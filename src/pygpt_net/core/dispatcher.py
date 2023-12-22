#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2023.12.18 04:00:00                  #
# ================================================== #


class Dispatcher:
    def __init__(self, window=None):
        """
        Event dispatcher

        :param window: Window instance
        """
        self.window = window

    def dispatch(self, event, all=False):
        """
        Dispatch event to plugins

        :param event: event to dispatch
        :param all: true if dispatch to all plugins (enabled or not)
        """
        for id in self.window.app.plugins.plugins:
            if self.window.controller.plugins.is_enabled(id) or all:
                if event.stop:
                    break
                self.apply(id, event)

    def apply(self, id, event):
        """
        Handle event in plugin with provided id

        :param id: plugin id
        :param event: event object
        """
        if id in self.window.app.plugins.plugins:
            try:
                self.window.app.plugins.plugins[id].handle(event)
            except AttributeError:
                pass


class Event:
    def __init__(self, name=None, data=None):
        """
        Event class

        :param name: event name
        :param data: event data
        """
        self.name = name
        self.data = data
        self.ctx = None
        self.stop = False