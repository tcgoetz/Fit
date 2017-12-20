#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging
from datetime import tzinfo, timedelta, datetime

from OutputData import OutputData


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class MonitoringInfoOutputData(OutputData):
    def __init__(self, files):
        self.field_names_list = ['timestamp', 'file', 'activity_type', 'resting_metabolic_rate', 'cycles_to_distance',
                                'cycles_to_calories'] 
        OutputData.__init__(self, files)

    def parse_message(self, filename, message):
        self.local_timestamp = message['local_timestamp']['value']
        activity_type = message['activity_type']['value']
        resting_metabolic_rate = message['resting_metabolic_rate']['value']
        cycles_to_distance = message['cycles_to_distance']['value']
        cycles_to_calories = message['cycles_to_calories']['value']
        if isinstance(activity_type, list):
            for index, type in enumerate(activity_type):
                entry = {
                    'filename'                  : filename,
                    'timestamp'                 : self.local_timestamp,
                    'activity_type'             : type,
                    'resting_metabolic_rate'    : resting_metabolic_rate,
                    'cycles_to_distance'        : cycles_to_distance[index],
                    'cycles_to_calories'        : cycles_to_calories[index]
                }
                self.entries.append(entry)

    def parse_messages(self, file):
        monitoring_info_messages = file['monitoring_info']
        if monitoring_info_messages:
            self.parse_message(file.filename, monitoring_info_messages[0])

