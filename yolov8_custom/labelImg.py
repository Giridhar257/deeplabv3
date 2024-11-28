def scroll_request(self, delta, orientation):
    bar = self.scrollBars[orientation]
    units = -1 if delta < 0 else 1
    bar.setValue(int(bar.value() + bar.singleStep() * units))
