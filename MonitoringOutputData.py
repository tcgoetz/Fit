#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging
from datetime import tzinfo, timedelta, datetime

from OutputData import OutputData
from FieldStats import *


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MonitoringOutputData(OutputData):
    _sleep_period_padding = 1

    def __init__(self, files, sleep_period):
        self.sleep_period = sleep_period

        self.heading_names_list = ['timestamp', 'activity_type'] 
        self.field_names_list = ['timestamp', 'activity_type'] 

        self._hourly_stats = {}
        self._daily_stats = {}
        self._device_daily_stats = {}
        self._device_hourly_stats = {}
        self._overall_stats = {}
        self._stats_headings = FieldStats.stat_names

        self.first_day = None
        self.last_day = None

        self.last_timestamp_16 = 0
        self.matched_timestamp_16 = 0

        self._last_intensity = 0

        OutputData.__init__(self, files)
        self.summarize_stats()

    def add_entry_field(self, entry, field_name, field_value, units=None):
        entry[field_name] = field_value

        if not field_name in self.field_names_list:
            logger.debug(field_name + ": " + str(units))
            self.field_names_list.append(field_name)
            if units:
                heading = field_name + " (" + units + ")"
            else:
                heading = field_name
            self.heading_names_list.append(heading)

    def parse_message(self, message, hourly_stats, daily_stats):
        entry = {}
        for field_name in message:
            field = message[field_name]

            if field_name == 'timestamp' or field_name == 'timestamp_16':
                self.last_timestamp = message.timestamp()
                self.add_entry_field(entry, 'timestamp', self.last_timestamp)
            else:
                if field_name == 'intensity':
                    self.last_intensity = field.value()
                elif field_name == 'heart_rate':
                    stat_name = "intensity_" + str(self.last_intensity) + "_hr"
                    hourly_stats._accumulate(stat_name, field.value(), FieldStats.stats_basic)
                    daily_stats._accumulate(stat_name, field.value(), FieldStats.stats_basic)

                self.add_entry_field(entry, field_name, field['display'], field.units())
                hourly_stats.hourly_accumulate(field_name, field)
                daily_stats.daily_accumulate(field_name, field)

        logger.debug(message.name() + ": " + str(entry))

        return entry

    def parse_messages(self, file):
        device = file.device()

        self.last_timestamp = file.time_created()

        day = self.last_timestamp.replace(hour=0, minute=0, second=0, microsecond=0)
        if not self.first_day:
            self.first_day = day
        self.last_day = day
        if not day in self._device_daily_stats.keys():
            self._device_daily_stats[day] = {}
        if not device in self._device_daily_stats[day].keys():
            self._device_daily_stats[day][device] = AggregateStats()
        daily_stats = self._device_daily_stats[day][device]

        monitoring_messages = file['monitoring']
        if monitoring_messages:
            for message in monitoring_messages:
                hour = self.last_timestamp.replace(minute=0, second=0, microsecond=0)
                if not hour in self._device_hourly_stats.keys():
                    self._device_hourly_stats[hour] = {}
                if not device in self._device_hourly_stats[hour].keys():
                    self._device_hourly_stats[hour][device] = AggregateStats()
                hourly_stats = self._device_hourly_stats[hour][device]

                self.entries.append(self.parse_message(message, hourly_stats, daily_stats))

        self.entries.sort(key=lambda item:item['timestamp'])

    def compute_overall_stats(self, day, stats_day):
        overall_cum_stats_fields = ['total_floors', 'total_steps']
        for overall_stats_field in overall_cum_stats_fields:
            if overall_stats_field in self._overall_stats.keys():
                self._overall_stats[overall_stats_field] = self.concatenate_fields(self._overall_stats[overall_stats_field], stats_day[overall_stats_field], True, False)
            else:
                self._overall_stats[overall_stats_field] = stats_day[overall_stats_field]
                self._overall_stats[overall_stats_field]['count'] = 1
                self._overall_stats[overall_stats_field]['avg'] = self._overall_stats[overall_stats_field]['total']

        overall_stats_fields = ['heart_rate', 'resting_heart_rate', 'intensity_mins']
        for overall_stats_field in overall_stats_fields:
            if overall_stats_field in stats_day.keys():
                if overall_stats_field in self._overall_stats.keys():
                    self._overall_stats[overall_stats_field] = \
                            self.concatenate_fields(self._overall_stats[overall_stats_field],
                                                    stats_day[overall_stats_field], True, True)
                else:
                    self._overall_stats[overall_stats_field] = stats_day[overall_stats_field]
                    self._overall_stats[overall_stats_field]['count'] = 1
                    self._overall_stats[overall_stats_field]['total'] = self._overall_stats[overall_stats_field]['avg']

    def concatenate_fields(self, first_field, second_field, overall_stat=False, sum_of_avg_stat=False):
        new_field = first_field

        if overall_stat:
            new_field['count'] = first_field['count'] + 1
        else:
            new_field['count'] = first_field['count'] + second_field['count']


        if sum_of_avg_stat:
            if first_field['max'] < second_field['max']:
                new_field['max'] = second_field['max']
            else:
                new_field['max'] = first_field['max']
            if first_field['min'] > second_field['min']:
                new_field['min'] = second_field['min']
            else:
                new_field['min'] = first_field['min']
            new_field['total'] = first_field['total'] + second_field['avg']
            new_field['avg'] = new_field['total'] / new_field['count']
        else:
            if first_field['min'] > second_field['min']:
                new_field['min'] = second_field['min']
            else:
                new_field['min'] = first_field['min']
            # is this a cumulative stat?
            if not second_field['total']:
                new_field['max'] = first_field['max'] + second_field['max']
                new_field['total'] = 0
                new_field['avg'] = 0
            else:
                if first_field['max'] < second_field['max']:
                    new_field['max'] = second_field['max']
                else:
                    new_field['max'] = first_field['max']
                new_field['total'] = first_field['total'] + second_field['total']
                new_field['avg'] = new_field['total'] / new_field['count']

        return new_field

    def concatenate_times(self, first_time_period, second_time_period):
        new_time_period = first_time_period

        for field_name in second_time_period:
            second_time_period_field = second_time_period[field_name]
            if field_name in first_time_period:
                first_time_period_field = first_time_period[field_name]
                if first_time_period_field['count'] == 0:
                    new_time_period[field_name] = second_time_period_field.copy()
                elif second_time_period_field['count'] == 0:
                    new_time_period[field_name] = first_time_period_field.copy()
                else:
                    new_time_period[field_name] = self.concatenate_fields(first_time_period_field, second_time_period_field)
            else:
                new_time_period[field_name] = second_time_period_field.copy()

        return new_time_period

    def summarize_time_stats(self, time_stats):
        sum_time_stats = {}
        for field_name in time_stats.keys():
            field_stats = time_stats[field_name]
            field_stats_values = field_stats.get()
            if field_stats_values:
                sum_time_stats[field_name] = field_stats_values
        return sum_time_stats

    def summarize_aggregate_stats(self, aggregate_dev_stats, aggregate_stats):
        times = aggregate_dev_stats.keys()
        for time in times:
            dev_time_stats = aggregate_dev_stats[time]
            for time_device in dev_time_stats.keys():
                device_stats = dev_time_stats[time_device]
                summed_device_stats = self.summarize_time_stats(device_stats)
                if time in aggregate_stats.keys():
                    aggregate_stats[time] = self.concatenate_times(aggregate_stats[time], summed_device_stats)
                else:
                    aggregate_stats[time] = summed_device_stats
            device_count = len(dev_time_stats.keys())
            if device_count > 1:
                aggregate_stats[time]['devices'] = {
                    'count' : device_count, 'max' : 0, 'avg' : 0, 'total' : device_count, 'min' : 0
                }

    def add_derived_hourly_stats(self):
        for hour in self._hourly_stats.keys():
            hour_integer = hour.hour
            if (hour_integer >= (self.sleep_period['end'] - self._sleep_period_padding) and
                hour_integer <= (self.sleep_period['end'] + self._sleep_period_padding)):
                stats_hour = self._hourly_stats[hour]
                if 'intensity_0_hr' in stats_hour.keys():
                    rhr_stat = stats_hour['intensity_0_hr']
                    self._hourly_stats[hour]['resting_heart_rate'] = rhr_stat.copy()
                    day = hour.replace(hour=0)
                    if day in self._daily_stats:
                        daily_stats = self._daily_stats[day]
                        if 'resting_heart_rate' in daily_stats.keys():
                            if rhr_stat['avg'] < daily_stats['resting_heart_rate']['avg']:
                                daily_stats['resting_heart_rate'] = rhr_stat.copy()
                        else:
                            daily_stats['resting_heart_rate'] = rhr_stat.copy()
                    else:
                        self._daily_stats[day] = {}
                        self._daily_stats[day]['resting_heart_rate'] = rhr_stat.copy()

    def add_derived_stats(self, stats_day):
        derived_stats = {
            'total_steps' : ['walking_steps', 'running_steps'],
            'total_floors' : ['cum_ascent_floors']
        }
        for derived_stat in derived_stats:
            component_stat_names = derived_stats[derived_stat]
            stat = { 'count' : 0, 'max' : 0, 'avg' : 0, 'total' : 0, 'min' : 0 }
            for component_stat_name in component_stat_names:
                if component_stat_name in stats_day.keys():
                    component_stat = stats_day[component_stat_name]
                    stat['count'] += component_stat['count']
                    stat['max'] = 0
                    stat['avg'] = 0
                    stat['total'] += int(component_stat['max'])
                    stat['min'] = 0
            stats_day[derived_stat] = stat

    def summarize_stats(self):
        self.summarize_aggregate_stats(self._device_daily_stats, self._daily_stats)

        self.summarize_aggregate_stats(self._device_hourly_stats, self._hourly_stats)
        self.add_derived_hourly_stats()

        for day in self._daily_stats:
            self.add_derived_stats(self._daily_stats[day])
            self.compute_overall_stats(day, self._daily_stats[day])

    def heading_names(self):
        return self.heading_names_list

    def get_stats_headings(self):
        return self._stats_headings

    def get_hourly_stats(self):
        return self._hourly_stats

    def get_daily_stats(self):
        return self._daily_stats

    def get_overall_stats(self):
        return self._overall_stats

    def get_date_span(self):
        return (self.first_day, self.last_day)