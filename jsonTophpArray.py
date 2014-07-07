import sublime, sublime_plugin,re

class jsonTophpArrayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		braces = False
		sels = self.view.sel()
		for sel in sels:
			if self.view.substr(sel).find('{') != -1:
				braces = True
		# self.view.insert(edit, 0, "Hello, World!")
		if not braces:
			new_sels = []
			for sel in sels:
				new_sels.append(self.view.find('\}', sel.end()))
			sels.clear()
			for sel in new_sels:
				sels.add(sel)
			self.view.run_command("expand_selection", {"to": "brackets"})
		php = self.convert(sels[0])
		print php
		self.view.insert(edit, sel.end(), "\n/*---- PHP Array ----*/\n"+php+"\n")

	def convert(self, json):
		string = self.view.substr(json)
		newString = re.sub(r'(^[#/]? *)var ',r'\1$',string)
		newString = re.sub(r'= ?{','= array(',newString)
		newString = re.sub(r'^ ?{','array(',newString)
		newString = re.sub(r': ?{','=> array(',newString)
		newString = re.sub(r': ?\[','=> array(',newString)
		newString = re.sub(r':','=>',newString)
		newString = re.sub(r'"','\'',newString)
		newString = re.sub(r'[}\]]',')',newString)
		return newString
		