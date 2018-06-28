#!/usr/bin/env python
# encoding: utf-8
import os
import logging
import logging.handlers


class Logger(object):
    log_name = 'MyFlask.log'
    log_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../%s' % log_name))
    log_size = 1024 * 1024 * 10
    log_num = 5
    log = logging.getLogger()
    formatter = logging.Formatter('[%(levelname)s] [%(asctime)s] %(message)s',
                                  '%Y-%m-%d %H:%M:%S')
    handle = logging.handlers.RotatingFileHandler(log_file, maxBytes=log_size, backupCount=log_num)
    handle.setFormatter(formatter)
    log.addHandler(handle)

    log.setLevel(logging.INFO)


    @classmethod
    def info(cls, msg):
        # cls.elk.info(msg)
        cls.log.info(msg)
        return

    @classmethod
    def warning(cls, msg):
        # cls.elk.warning(msg)
        cls.log.warning(msg)
        return

    @classmethod
    def error(cls, msg):
        # cls.elk.error(msg)
        cls.log.error(msg)
        return

    @classmethod
    def debug(cls, msg):
        # cls.elk.debug(msg)
        cls.log.debug(msg)
        return
