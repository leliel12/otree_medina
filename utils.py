#!/usr/bin/env python
# -*- coding: utf-8 -*-

import otree.constants_internal as constants

def float_as_percentage(a):
        return int(a * 100)


class TimeOutMixin(object):

    process_form_on_timeout = False

    def post(self, request, *args, **kwargs):

        self.object = self.get_object()

        if request.POST.get(constants.auto_submit):
            self.timeout_happened = True  # for public API
        else:
            self.timeout_happened = False

        if self.timeout_happened == False or self.process_form_on_timeout:
            form = self.get_form(
                data=request.POST, files=request.FILES, instance=self.object)
            if form.is_valid():
                self.form = form
                self.object = form.save()
            elif self.PROCESS_FORM_ON_TIMEOUT:
                self._set_auto_submit_values()
            else:
                return self.form_invalid(form)
        else:
            self._set_auto_submit_values()

        self.before_next_page()
        self._increment_index_in_pages()
        return self._redirect_to_page_the_user_should_be_on()
