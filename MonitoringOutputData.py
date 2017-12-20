#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging
from datetime import tzinfo, timedelta, datetime

from OutputData import OutputData


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MonitoringOutputData(OutputData):
    _sleep_period_padding = 1

    def __init__(self, files):
        self.field_names_list = ['timestamp', 'activity_type'] 

        self.first_day = None
        self.last_day = None

        self.last_timestamp_16 = 0
        self.matched_timestamp_16 = 0

        OutputData.__init__(self, files)

    def add_entry_field(self, entry, field_name, field_value, units=None):
        entry[field_name] = field_value

        if not field_name in self.field_names_list:
            logger.debug(field_name + ": " + str(units))
            self.field_names_list.append(field_name)

    def parse_message(self, message):
        entry = {}
        for field_name in message:
            field = message[field_name]

            if field_name == 'timestamp' or field_name == 'timestamp_16':
                self.last_timestamp = message.timestamp()
                self.add_entry_field(entry, 'timestamp', self.last_timestamp)
            else:
               self.add_entry_field(entry, field_name, field.value(), field.units())

        logger.debug(message.name() + ": " + str(entry))

        return entry

    def parse_messages(self, file):
        self.last_timestamp = file.time_created()

        monitoring_messages = file['monitoring']
        if monitoring_messages:
            for message in monitoring_messages:
                self.entries.append(self.parse_message(message))

        self.entries.sort(key=lambda item:item['timestamp'])

    def get_date_span(self):
        return (self.first_day, self.last_day)