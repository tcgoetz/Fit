#!/usr/bin/env python

#
# copyright Tom Goetz
#

import logging
from datetime import tzinfo, timedelta, datetime

from OutputData import OutputData


logger = logging.getLogger(__name__)


class MonitoringOutputData(OutputData):

    def __init__(self, files):
        OutputData.__init__(self, files)

    def parse_message(self, message):
        entry = {}
        for field_name, field in message.iteritems():
            if field_name == 'timestamp_16':
                entry['timestamp'] = message.timestamp()
            else:
                entry[field_name] = field.value()
        logger.debug(message.name() + ": " + str(entry))
        return entry

    def parse_messages(self, file):
        monitoring_messages = file['monitoring']
        if monitoring_messages:
            for message in monitoring_messages:
                self.entries.append(self.parse_message(message))
