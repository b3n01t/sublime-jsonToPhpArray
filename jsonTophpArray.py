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
				new_sels.append(self.view.find('\{', sel.end()))
			sels.clear()
			for sel in new_sels:
				sels.add(sel)
			self.view.run_command("expand_selection", {"to": "brackets"})
		
		converted = self.convert(sels[0])
		name = converted[0]+'_array.php'
		php = converted[1]

		openViews =  self.view.window().views()
		newView = None
		for v in openViews:
			if v.name() == name:
				newView = v
				break


		newView = newView and newView or self.view.window().new_file()
		
		newView.set_syntax_file('Packages/PHP/PHP.tmLanguage')
		newView.set_name(name)
		newView.insert(edit, 0, "<?php\n/*---- PHP Array ----*/\n"+php+"\n?>")
		self.view.window().focus_view(newView)

	def convert(self, json):
		string = self.view.substr(json)
		name = re.search(r'var (.*) ?=',string)
		name = name and name.group(1) or 'PHP_Array'
		newString = re.sub(r'([#/]? *)var ',r'\1$',string)
		newString = re.sub(r'= ?{','= array(',newString)
		newString = re.sub(r'[ \t]*{','array(',newString)
		newString = re.sub(r': ?{','=> array(',newString)
		newString = re.sub(r': ?\[','=> array(',newString)
		newString = re.sub(r':','=>',newString)
		newString = re.sub(r'["]','\'',newString)
		newString = re.sub(r'([ \t\n]*)([^"\'\t ].*[^"\' \t]) ?=>',r"\1'\2'=>",newString)
		newString = re.sub(r'[}\]]',')',newString)
		newString = re.sub(r';?$',';',newString)
		return (name.strip(),newString)
		