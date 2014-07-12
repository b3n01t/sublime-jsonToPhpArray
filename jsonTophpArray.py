import sublime, sublime_plugin,re

class jsonTophpArrayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
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
		newView.insert(edit, 0, "<?php\n/*---- PHP Array ----*/\n"+php+"\n\n?>")
		if self.view.window():
			self.view.window().focus_view(newView)

	def convert(self, json):
		string = self.view.substr(json)
		string = string.strip()
		name = re.search(r'(var)? ?(.*) ?=',string)
		print(name.groups())
		name = name and name.group(2) or 'PHP_Array'
		newString = re.sub(r'([#/]? *)var ',r'\1$',string)
		newString = re.sub(r'= ?{','= array(',newString)
		newString = re.sub(r'[ \t]*{','array(',newString)
		newString = re.sub(r': ?{','=> array(',newString)
		newString = re.sub(r': ?\[','=> array(',newString)
		newString = re.sub(r':','=>',newString)
		newString = re.sub(r'["]','\'',newString)
		newString = re.sub(r'([ \t\n]*)([^"\'\t ].*[^"\' \t]) ?=>',r"\1'\2'=>",newString)
		newString = re.sub(r'[}\]]',')',newString)
		newString = re.sub(r'\)([ \t\n]*)\$',r");\1$",newString)
		newString = re.sub(r'\);?$',r");",newString)
		return (name.strip(),newString)
		