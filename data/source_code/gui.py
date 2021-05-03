import json_handler as jh
from tkinter import *
from tkinter import ttk
from tkinter import colorchooser as cck
import os
from os import path
from os.path import isfile
from subprocess import call

global end_it_all
end_it_all = 'no'

font, text_font = 'Segoe UI Light', 'Arial'

global custom_settings
custom_settings = jh.open_file("data/preferences.json")

global colors
colors = custom_settings['colors']

global allowed_char
allowed_char = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_- "))

bg, text, fg, highlight, d_bg = colors['background'], colors['highlights'],colors['foreground'], colors['treeview secondary'], colors['alternate background']

def get_files(path):
	patches = []
	for file in os.listdir(path):
		if file.endswith(".vital"):
			patches.append(file)
	return patches
# Edit GUI
def edit():
	both = jh.open_file('data/customs.json')
	global prefix
	global style2
	prefix = both['prefix']
	style2 = both['style']

	#Actual Gui

	edit = Toplevel()
	edit.title("Edit Customs")
	edit.config(bg = bg)

	#style
	style = ttk.Style(edit)
	style.theme_use("default")

	style.configure("Treeview",
		background = bg,
		foreground = d_bg,
		rowheight = 25,
		fieldbackground = d_bg
		)

	style.map("Treeview",
		background = [('selected', bg)]
		)

	add_icon = PhotoImage(file = 'data/add_icon.gif')
	subtract_icon = PhotoImage(file = 'data/subtract_icon.gif')

	#Prefix
	pref = ttk.Treeview(edit, height = 15)
	pref['columns'] = 'Prefix'

	pref.column("#0", width = 0, stretch = NO)
	pref.column("Prefix", width = 100, stretch = NO)

	pref.heading("#0", text = "", anchor = W)
	pref.heading("Prefix", text = "Prefix", anchor = W)

	#Striped Rows
	pref.tag_configure("oddrow", background = fg)
	pref.tag_configure("evenrow", background = highlight)


	def reload_pref():
		pref.delete(*pref.get_children())
		count = 0
		for pre in prefix:
			if count % 2 == 0:
				pref.insert(parent = '', index = 'end', iid = count, text = "", value = (prefix[count],), tags = ('oddrow',))
			else:
				pref.insert(parent = '', index = 'end', iid = count, text = "", value = (prefix[count],), tags = ('evenrow',))
			count += 1
	reload_pref()

	pref.grid(row =0, column = 0, sticky = NW, padx = 10, pady = 10)

	#style
	styles = ttk.Treeview(edit, height = 15)
	styles['columns'] = 'Style'

	styles.column("#0", width = 0, stretch = NO)
	styles.column("Style", width = 100, stretch = NO)

	styles.heading("#0", text = "", anchor = W)
	styles.heading("Style", text = "Style", anchor = W)

	#Striped Rows
	styles.tag_configure("oddrow", background = fg)
	styles.tag_configure("evenrow", background = highlight)

	def reload_style():
		styles.delete(*styles.get_children())
		count = 0
		for pre in style2:
			if count % 2 == 0:
				styles.insert(parent = '', index = 'end', iid = count, text = "", value = (style2[count],), tags = ('oddrow',))
			else:
				styles.insert(parent = '', index = 'end', iid = count, text = "", value = (style2[count],), tags = ('evenrow',))
			count += 1
	reload_style()

	styles.grid(row =0, column = 1, sticky = NW, padx = 10, pady = 10)

	#insertions
	def add_new_pref():
		if (add_pref.get()).strip() != '':
			prefix.append(add_pref.get().strip())
			reload_pref()
	def add_new_style():
		if (add_style.get()).strip() != '':
			style2.append(add_style.get().strip())
			reload_style()
	def remove_pref():
		try:
			prefix.remove(add_pref.get())
			reload_pref()
		except Exception:
			pass
	def remove_style():
		try:
			style2.remove(add_style.get())
			reload_style()
		except Exception:
			pass
	def set_pref(event):
		add_pref.delete(0, END)
		add_pref.insert(0, prefix[int(pref.focus())])
	def set_style(event):
		add_style.delete(0, END)
		add_style.insert(0, style2[int(styles.focus())])
	def save():
		both = {"prefix":prefix, "style":style2}
		jh.write_file('data/customs.json', jh.dict_json(both))
		c_style = style2
		c_pref = prefix

		Label(edit, text = 'You will need to reload the program\nfor your changes to appear\nin the drop menus', bg = bg, fg = fg) .grid(row = 8, column = 0, columnspan = 2)

	def exit_edit():
		edit.destroy()

	pref.bind('<<TreeviewSelect>>', set_pref)
	styles.bind('<<TreeviewSelect>>', set_style)
	#prefix
	add_pref = Entry(edit, width = 15, relief = FLAT) 
	add_pref.grid(row = 1, column = 0, sticky = NSEW, pady = 10)
	Button(edit, image = add_icon, command = add_new_pref) .grid(row = 2, column = 0, sticky = NSEW) #Change to plus image
	Button(edit, image = subtract_icon, command = remove_pref) .grid(row = 3, column = 0, sticky = NSEW) #Change to minus image	

	add_style = Entry(edit, width = 15, relief = FLAT) 
	add_style.grid(row = 1, column = 1, sticky = NSEW, pady = 10)
	Button(edit, image = add_icon, command = add_new_style) .grid(row = 2, column = 1, sticky = NSEW) #Change to plus image
	Button(edit, image = subtract_icon, command = remove_style) .grid(row = 3, column = 1, sticky = NSEW) #Change to minus image	
	
	Button(edit, text = 'Save', command = save) .grid(row = 4, column = 0, sticky = NSEW, columnspan = 2)

	Button(edit, text = 'Exit', command = exit_edit) .grid(row = 5, column = 0, sticky = NSEW, columnspan = 2)

	edit.mainloop()

# Edit Preferences
def settings_edit():
	global colors
	global custom_settings

	current_preferences = jh.open_file("data/preferences.json")


	preferences = Toplevel()
	preferences.title('Edit Preferences and settings')
	preferences.config(bg = bg)

	Label(preferences, text = 'Edit colors', bg = bg, fg = fg) .grid(row = 0)
	Label(preferences, text = 'Replace duplicate prefixes?', bg = bg, fg = fg) .grid(row = 3)
	Label(preferences, text = 'Repair nameless presets?', bg = bg, fg = fg) .grid(row = 4)
	Label(preferences, text = 'Custom whitespace character:', bg = bg, fg = fg) .grid(row = 6)
	Label(preferences, text = 'Default break character:', bg = bg, fg = fg) .grid(row = 7)

	def edit_selected_color():
		to_edit = edit_color_hold.get()
		color_code = cck.askcolor(title = to_edit)
		colors[to_edit] = color_code[1]

	def save():
		custom_settings['colors'] == colors
		custom_settings['replace_duplicate_prefix'] = replace_duplicates.get()
		custom_settings['whitespace_character'] = whitespace_character.get().strip()
		custom_settings['default_break'] = default_break.get().strip()
		custom_settings['repair_broken'] = repair_broken.get()

		jh.write_file('data/preferences.json', custom_settings)
		Label(preferences, text = 'Changes will go into effect after reopening the program', bg = bg, fg = fg) .grid(row = 10, columnspan = 2)

	def reset():
		custom_settings['colors'] = custom_settings['default']['colors']
		custom_settings['replace_duplicate_prefix'] = custom_settings['default']['replace_duplicate_prefix']
		custom_settings['whitespace_character'] = custom_settings['default']['whitespace_character']
		custom_settings['default_break'] = custom_settings['default']['default_break']
		custom_settings['repair_broken'] = custom_settings['default']['repair_broken']

		jh.write_file('data/preferences.json', custom_settings)
		Label(preferences, text = 'Changes will go into effect after reopening the program', bg = bg, fg = fg) .grid(row = 10, columnspan = 2)

	def exit():
		preferences.withdraw()
		preferences.destroy()

	edit_color_hold = StringVar()
	edit_color = OptionMenu(preferences, edit_color_hold, *colors.keys())
	edit_color.config(relief = SUNKEN, bd = 0)
	edit_color.grid(row = 1, column = 0)

	Button(preferences, text = 'Edit', command = edit_selected_color) .grid(row = 1, column = 1, sticky = W, padx = 3)
	Button(preferences, text = 'Save', command = save) .grid(row = 8)
	Button(preferences, text = 'Reset to Defaults', command = reset) .grid(row = 8, column = 1, padx = 3)
	Button(preferences, text = 'Exit', command = exit) .grid(row = 9, column = 0, columnspan = 2, sticky = NSEW, pady = 3, padx = 3)

	repair_broken = StringVar()
	repair_broken.set(custom_settings['repair_broken'])
	Checkbutton(preferences, var = repair_broken, activebackground = bg, bg = bg, fg = bg, relief = FLAT) .grid(row = 4, column = 1, sticky = W)

	replace_duplicates = StringVar()
	replace_duplicates.set(custom_settings['replace_duplicate_prefix'])
	Checkbutton(preferences, var = replace_duplicates, activebackground = bg, bg = bg, fg = bg, relief = FLAT) .grid(row = 3, column = 1, sticky = W)

	whitespace_character = Entry(preferences, width = 2)
	whitespace_character.insert(0, custom_settings['whitespace_character'])
	whitespace_character.grid(row = 6, column = 1, sticky = W, padx = 3, pady = 3)

	default_break = Entry(preferences, width = 2)
	default_break.insert(0, custom_settings['default_break'])
	default_break.grid(row = 7, column = 1, sticky = W, padx = 3, pady = 3)

	preferences.mainloop()

# Main GUI
def gui():
	#Variables
	end_it_all = 'no'
	settings = [{}]
	data = {}
	customs = jh.open_file('data/customs.json')
	global c_pref
	global c_style
	c_pref = customs['prefix']
	c_style = customs['style']

	files = get_files("PRESETS_HERE")

	# Configs
	main = Tk()
	main.title('EasyEdits')
	main.config(bg = bg)

	#Progress Bar

	def start():
		progress.start(5)
	def end():
		progress.stop()

	progress = ttk.Progressbar(main, orient = VERTICAL, mode = 'indeterminate')
	progress.grid(row = 0, column = 2, rowspan = 2, sticky = NS, pady = 10)

	# Image Labeling
	file_icon = PhotoImage(file = 'data/file_icon.gif')
	vital_tools = PhotoImage(file = 'data/vital_tools.gif')
	save_icon = PhotoImage(file = 'data/save_icon.gif')
	edit_icon = PhotoImage(file = 'data/edit_icon.gif')
	gear_icon = PhotoImage(file = 'data/gear_icon.gif')
	options_icon = PhotoImage(file = 'data/options_icon.gif')
	right_arrow = PhotoImage(file = 'data/right_arrow.gif')
	left_arrow = PhotoImage(file = 'data/left_arrow.gif')

	# Defnie Tree style
	style = ttk.Style()
	style.theme_use("default")

	style.configure("Treeview",
		background = bg,
		foreground = fg,
		rowheight = 25,
		fieldbackground = d_bg
		)
	style.configure("TProgressbar",
		background = fg,
		troughcolor = d_bg,
		troughrelief = FLAT,
		thumbrelief = FLAT
		)

	style.map("Treeview",
		background = [('selected', bg)]
		)

	# Define/Format Treeview
	data_list = ttk.Treeview(main)

	#Columns
	data_list['columns'] = ('Name','Author','Style','Description')

	data_list.column("#0", width = 20, stretch = NO)
	data_list.column('Name', anchor = W, width = 90, minwidth = 35)
	data_list.column('Author', anchor = W, width = 60, minwidth = 35)
	data_list.column('Style', anchor = W, width = 60, minwidth = 35)
	data_list.column('Description', anchor = W, width = 350, minwidth = 225)

	data_list.heading("#0", text = "File", anchor = W)
	data_list.heading("Name", text = "Name", anchor = W)
	data_list.heading("Author", text = "Author", anchor = W)
	data_list.heading("Style", text = "Style", anchor = W)
	data_list.heading("Description", text = "Description", anchor = W)

	#Striped Rows
	data_list.tag_configure("oddrow", background = fg)
	data_list.tag_configure("evenrow", background = highlight)

	problems = []
	x = 0
	count = 0
	for file in files:
		yn = 1
		patch_data = jh.open_file(f'PRESETS_HERE/{file}')
		try:
			tmp = str(patch_data['preset_name'])
		except Exception:
			if custom_settings['repair_broken'] == "1":
				patch_data['preset_name'] = file.replace('.vital','')
			else:
				problems.append(file)
				yn = 0
		if yn == 1:
			try:
				data[file] = [str(patch_data['preset_name']), patch_data['author'], patch_data['preset_style'], patch_data['comments']]
			except Exception:
				problems.append(file)

			if count % 2 == 0:
				try:
					data_list.insert(parent = '', index = 'end', iid = x, text = file, value = (str(patch_data['preset_name']), patch_data['author'], patch_data['preset_style'], patch_data['comments']), tags = ('oddrow',))
				except Exception:
					pass
			else:
				try:
					data_list.insert(parent = '', index = 'end', iid = x, text = file, value = (str(patch_data['preset_name']), patch_data['author'], patch_data['preset_style'], patch_data['comments']), tags = ('evenrow',))
				except Exception:
					pass
		x += 1
		count += 1


	# Bind mini_view
	def mini_view_set(event):
		start()
		mini_view.delete(*mini_view.get_children())
		x = 0
		count = 0
		for file in data_list.selection():
			if count % 2 == 0:
				mini_view.insert(parent = '', index = 'end', iid = x, text = "Preset", value = data[files[int(file)]], tags = ('oddrow',))
			else:
				mini_view.insert(parent = '', index = 'end', iid = x, text = "Preset", value = data[files[int(file)]], tags = ('evenrow',))
			x += 1
			count += 1
		if len(data_list.selection()) != 0:
			mini_view.selection_set(0)
			mini_view.focus(0)
		end()


	data_list.bind('<<TreeviewSelect>>', mini_view_set)
	# Display Treeview
	data_list.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)

	def find(look_in, valuee):
		start()
		select = []
		x = 0
		for file in data:
			if valuee.lower() in data[file][look_in].lower():
				select.append(x)
			x += 1
		data_list.selection_set(select)
		return select
		end()
	# Select Things
	def s_name():
		start()
		value_box = value.get()
		select = find(0,value_box)
		end()
	def s_author():
		start()
		value_box = value.get()
		select = find(1,value_box)
		end()
	def s_style():
		start()
		value_box = value.get()
		select = find(2,value_box)
		end()
	def s_description():
		start()
		value_box = value.get()
		select = find(3,value_box)
		end()
	def see_selected():
		start()
		selected = data_list.selection()
		print(selected)
		end()
	def prefix_find(patch_info):
		start()
		prefix_find = ''
		char = break_char.get(1.0, 2.0).strip() # this .strip() is the result of 20 minutes of pure suffering... I hate this
		if char == custom_settings['whitespace_character']:
			char = ' '

		for x in patch_info[0]:

			if x == char:
				prefix_find += x
				break
			else:
				prefix_find += x

		if prefix_find == patch_info[0]:
			prefix_find = ''

		end()
		return prefix_find
	def r_set_selected():
		start()
		selected = mini_view.selection()
		if selected != ():
			tmp = mini_view.item(mini_view.focus())
			patch_info = data[str(tmp['values'][0]) + '.vital'] # Name, Author, Style, description
			pref = prefix_find(patch_info)

			# Set data
			prefix.delete(1.0,'end')
			if int(checks[0].get()) != 1:
				prefix.insert(1.0,pref)
			else:
				prefix.insert(1.0, pref_hold.get())
			name.delete(1.0,'end')
			name.insert(1.0,patch_info[0].replace(pref, ''))
			author.delete(1.0,'end')
			author.insert(1.0,patch_info[1])
			style.delete(1.0,'end')
			style.insert(1.0,patch_info[2])
			description.delete(1.0,'end')
			description.insert(1.0,patch_info[3])

			# preview name
			preview_text = preview_changes()
			preview.config(text = preview_text[0])
		end()
	def set_selected(event):
		r_set_selected()

	def update_pref(*args):
		start()
		prefix.delete(1.0,'end')
		prefix.insert(1.0,pref_hold.get())
		end()
	def update_style(*args):
		start()
		style.delete(1.0,'end')
		style.insert(1.0,style_hold.get())
		end()
	def edit_custom():
		edit()
	def launch_current():
		start()
		try:
			current = mini_view.item(int(mini_view.focus()))
			call(('cmd', '/c', 'start', '', f"PRESETS_HERE\\{current['values'][0]}.vital"))
		except ValueError:
			pass
		end()
	def save_prefs():
		start()
		if prefix.get(1.0, END).strip().replace(custom_settings['whitespace_character'], ' ') != '':
			c_pref.append(prefix.get(1.0, END).strip().replace(custom_settings['whitespace_character'], ' '))
			both = {"prefix":c_pref, "style":c_style}
			jh.write_file('data/customs.json', jh.dict_json(both))
			Label(out_frame, text = 'Customs styles and prefixes\nwill not reload until you\n reopen the program', bg = d_bg, fg = fg) .grid(row = 5, column = 1)
		end()
	def save_styles():
		start()
		if style.get(1.0, END).strip() != '':
			c_style.append(style.get(1.0, END).strip())
			both = {"prefix":c_pref, "style":c_style}
			jh.write_file('data/customs.json', jh.dict_json(both))
		end()
	
	def preview_changes():
		start()
		originals = combine_name(mini_view.item(mini_view.focus())['values'])
		end()
		return originals
	def update_things():
		start()
		r_set_selected()
		preview_changes()
		end()
	def focus_left():
		start()
		if len(mini_view.selection()) > 0:
			select_from = mini_view.selection()
			selected_index = int(mini_view.selection().index(mini_view.focus()))
			mini_view.focus(select_from[selected_index-1])
			update_things()
		end()
	def focus_right():
		start()
		if len(mini_view.selection()) > 0:
			select_from = mini_view.selection()
			selected_index = int(mini_view.selection().index(mini_view.focus()))
			if selected_index < len(select_from)-1:
				mini_view.focus(select_from[selected_index+1])
			else:
				mini_view.focus(select_from[0])
			update_things()
		end()
	# Add in selection buttons

	Label(main, text = 'Select by Value                                          Value here:', bg = bg, fg = fg) .grid(row = 1, column = 0, sticky = SW, padx = 20)
	select_frame = Frame(main, bg = bg)
	Button(select_frame, text = 'Name', command = s_name).grid(row = 0, column = 0)
	Button(select_frame, text = 'Author', command = s_author).grid(row = 0, column = 1)
	Button(select_frame, text = 'Style', command = s_style).grid(row = 0, column = 2)
	Button(select_frame, text = 'Description', command = s_description).grid(row = 0, column = 3)
	value = Entry(select_frame) 
	value.grid(row = 0, column = 4, padx = 10)

	select_frame.grid(row = 2, column = 0, sticky = NW, padx = 10)

	# Output data for editing

	out_frame = Frame(main, bg = d_bg, bd = 10)
	Label(out_frame, text = 'Prefix:', bg = d_bg, fg = fg) .grid(row = 0, column = 0, sticky = E)

	#prefix frame
	pref_frame = Frame(out_frame, bg = d_bg)
	prefix = Text(pref_frame, height = 1, width = 6, font = (font, 8, 'bold')) 
	prefix.grid(row = 0, column = 0, sticky = NSEW)

	#custom prefix dropdown
	pref_hold = StringVar()
	global pref_type
	pref_type = OptionMenu(pref_frame, pref_hold, *c_pref)
	pref_type.config(relief = SUNKEN, bd = 0)
	pref_type.grid(row = 0, column = 1, sticky = W, padx = 3)
	pref_hold.trace('w', update_pref)
	Button(pref_frame, image = save_icon, relief = FLAT, command = save_prefs) .grid(row = 0, column = 2, sticky = NSEW)

	#custom break character
	Label(out_frame, text = 'break:', bg = d_bg, fg = fg) .grid(row = 1, column = 0, sticky = E)
	break_char = Text(out_frame, height = 1, width = 2, font = (font, 8, 'bold'))
	break_char.grid(row = 1, column = 1, sticky = W)
	break_char.insert(1.0, custom_settings['default_break'])
	pref_frame.grid(row = 0, column = 1, sticky = W)

	#Append or Replace
	pref_change = StringVar()
	pref_change.set(0)
	change = Checkbutton(out_frame, var = pref_change, activebackground = d_bg, bg = d_bg) 
	change.grid(row = 2, column = 1, sticky = W)
	Label(out_frame, text = 'Replace?', bg = d_bg, fg = fg,) .grid(row = 2, column = 0, sticky = E)

	# Edit customs
	Button(pref_frame, image = edit_icon, relief = FLAT, command = edit_custom) .grid(row = 0, column = 3, sticky = NSEW)

	# Name Section
	Label(out_frame, text = 'Name:', bg = d_bg, fg = fg) .grid(row = 0, column = 3, sticky = E)
	name = Text(out_frame, height = 1, width = 15, font = (font, 8, 'bold')) 
	name.grid(row = 0, column = 4, sticky = W)

	# Author Section
	Label(out_frame, text = 'Author:', bg = d_bg, fg = fg) .grid(row = 1, column = 3, sticky = E)
	author = Text(out_frame, height = 1, width = 15, font = (font, 8, 'bold')) 
	author.grid(row = 1, column = 4, sticky = W)

	# Style section, contains frames
	Label(out_frame, text = 'Style:', bg = d_bg, fg = fg) .grid(row = 2, column = 3, sticky = E)

	#custom style sropdown
	style_frame = Frame(out_frame, bg = d_bg)
	Button(style_frame, image = edit_icon, relief = FLAT, command = edit_custom) .grid(row = 0, column = 3, sticky = NSEW)
	style = Text(style_frame, height = 1, width = 10, font = (font, 8, 'bold')) 
	style.grid(row = 0, column = 0, sticky = NSEW)

	# Label(style_frame, text = 'Saved', bg = bg, fg = fg) .grid(row = 0, column = 0, sticky = E)
	style_hold = StringVar()
	global style_type
	style_type = OptionMenu(style_frame, style_hold, *c_style, command = update_style)
	style_type.config(relief = FLAT, bd = 0)

	#save stuff
	style_type.grid(row = 0, column = 1, sticky = W, padx = 3)
	style_hold.trace('w', update_style)
	Button(style_frame, image = save_icon, relief = FLAT, command = save_styles) .grid(row = 0, column = 2, sticky = NSEW)
	style_frame.grid(row = 2, column = 4, sticky = W)

	#description section
	Label(out_frame, text = 'Description:', bg = d_bg, fg = fg) .grid(row = 5, column = 3, sticky = N)
	description = Text(out_frame, height = 8, width = 30, font = (font, 8, 'bold')) 
	description.grid(row = 5, column = 4, sticky = NSEW, pady = 3)

	global preview
	global preview_text
	preview_text = 'hi'
	preview = Label(out_frame, text = preview_text, bg = fg, fg = bg)
	preview.grid(row = 6, column = 1, sticky = NSEW)

	Button(out_frame, image = right_arrow, relief = FLAT, command = focus_right) .grid(row = 6, column =2, sticky = W)
	Button(out_frame, image = left_arrow, relief = FLAT, command =  focus_left) .grid(row = 6, column =0, sticky = E)

	#Checkboxes for not changing
	checks = [] # Prefix, Name, Author, Style, Description
	for x in range(5):
		checks.append(StringVar())
		checks[x].set('0')
	Checkbutton(out_frame, var = checks[0], activebackground = d_bg, bg = d_bg, fg = d_bg, relief = FLAT).grid(row = 0, column = 2, sticky = NSEW)
	Checkbutton(out_frame, var = checks[1], activebackground = d_bg, bg = d_bg, fg = d_bg, relief = FLAT).grid(row = 0, column = 5, sticky = NSEW)
	Checkbutton(out_frame, var = checks[2], activebackground = d_bg, bg = d_bg, fg = d_bg, relief = FLAT).grid(row = 1, column = 5, sticky = NSEW)
	Checkbutton(out_frame, var = checks[3], activebackground = d_bg, bg = d_bg, fg = d_bg, relief = FLAT).grid(row = 2, column = 5, sticky = NSEW)
	Checkbutton(out_frame, var = checks[4], activebackground = d_bg, bg = d_bg, fg = d_bg, relief = FLAT).grid(row = 5, column = 5, sticky = NW)
	#Label(out_frame, text = 'Checkboxes will determine which\nvalues are affected when\n"APPLY TO SELECTED" is pressed', bg = d_bg, fg = fg) .grid(row = 5, column = 1, sticky = SW)

	# Mini Treeview
	mini_view = ttk.Treeview(main, height = 10)
	mini_view['columns'] = ('Preset')
	#set columns
	mini_view.column('#0', width = 0, stretch = NO)
	mini_view.column('Preset', width = 180, anchor = W)
	#headers
	mini_view.heading("#0", text = "X", anchor = W)
	mini_view.heading('Preset', text = "Preset", anchor = W)

	mini_view.bind('<<TreeviewSelect>>', set_selected)
	mini_view.grid(row = 0, column = 1, sticky = NW, padx = 10, pady = 10)

	def select_all():
		start()
		select = []
		y = 0
		for x in data_list.selection():
			select.append(y)
			y += 1
		mini_view.selection_set(select)
		if len(mini_view.selection()) > 0:
			mini_view.focus(mini_view.selection()[0])
		end()
	def select_invert():
		start()
		select = []
		x = mini_view.selection()
		z = 0
		for y in mini_view.get_children():
			if y in x:
				pass
			else:
				select.append(y)
			z+=1
		mini_view.selection_set(select)
		if len(mini_view.selection()) > 0:
			mini_view.focus(mini_view.selection()[0])
		end()
	def select_below():
		start()
		select = []
		for x in range(len(mini_view.get_children())):
			if str(x) >= mini_view.focus():
				select.append(x)
		mini_view.selection_set(select)
		if len(mini_view.selection()) > 0:
			mini_view.focus(mini_view.selection()[0])
		end()
	def select_above():
		start()
		select = []
		for x in range(len(mini_view.get_children())):
			if str(x) <= mini_view.focus():
				select.append(x)
		mini_view.selection_set(select)
		if len(mini_view.selection()) > 0:
			mini_view.focus(mini_view.selection()[0])
		end()

	#Launch currentyl sleelceteofjekfbdwajhfh
	launch = Frame(main, bg = d_bg)
	#Label(launch, text = 'View:', bg = d_bg, fg = fg) .grid(row = 0, column = 0, sticky = W)
	Button(launch, image = gear_icon, command = launch_current, relief = FLAT) .grid(row = 0, column = 0, sticky = NW)
	Button(launch, text = 'All', command = select_all, relief = FLAT) .grid(row = 0, column = 1, sticky = NW)
	Button(launch, text = 'Invert', command = select_invert, relief = FLAT) .grid(row = 0, column = 2, sticky = NW)
	Button(launch, text = 'Below', command = select_below, relief = FLAT) .grid(row = 0, column = 3, sticky = NW)
	Button(launch, text = 'Above', command = select_above, relief = FLAT) .grid(row = 0, column = 4, sticky = NSEW)
	launch.grid(row = 1, column = 1, sticky = W, padx = 10)

	mini_view.tag_configure("oddrow", background = fg)
	mini_view.tag_configure("evenrow", background = highlight)
	
	out_frame.grid(row = 3, column = 0, pady = 10, sticky = N)

	Button(main, image = vital_tools, bg = bg, activebackground = bg, relief = FLAT, command = start) .grid(row = 3, column = 1, sticky = NSEW, padx = 10)

	def find_oPref(name):
		start()
		sever = break_char.get(1.0, 2.0).strip()
		new_prefix = ''
		for x in name:
			if x != sever:
				new_prefix += x
			else:
				new_prefix += x
				return new_prefix
		end()
	def combine_name(item_data):
		start()
		new_name = name.get(1.0, END).strip()
		new_prefix = prefix.get(1.0, END).strip('\n').replace(custom_settings['whitespace_character'], ' ')
		original_prefix = '' if find_oPref(str(item_data[0])) is None else find_oPref(str(item_data[0]))
		original_name = item_data[0]
		store = []

		if checks[1].get() == '1':

			if checks[0].get() == '1':

				if pref_change.get() == '1':
					store.append(new_prefix + new_name)

				else:
					if custom_settings['replace_duplicate_prefix'] == '1':

						if new_prefix == original_prefix:
							store.append(new_prefix + new_name)

						else:
							store.append(new_prefix + original_prefix + new_name)

					else:
						store.append(new_prefix + new_name)

			else:
				store.append(original_prefix + new_name)

		else:
			if checks[0].get() == '1':

				if pref_change.get() == '1':

					if str(original_prefix) != 'None':
						store.append(new_prefix + original_name.replace(original_prefix, '', 1))	

					else:
						store.append(original_name.replace(original_prefix, new_prefix, 1))

				else:
					if custom_settings['replace_duplicate_prefix'] == '1':
						store.append(new_prefix + original_name)
					else:
						store.append(new_prefix + original_name.replace(original_prefix, '', 1))

			else:
				store.append(original_name)

		end()
		if_allowed = set((store[0]))
		if if_allowed.issubset(allowed_char):
			pass
		else:
			store[0] = 'Contains Illegal Chars'
		return store
	# Submit data, oh boy
	def apply_data():
		new = []
		illegal = 'no'
		for x in mini_view.selection():
			new = []
			originals = mini_view.item(x)['values'] # Name, Author, Style, Comments
			new.append(combine_name(originals)[0])
			if new[0] != "Contains Illegal Chars":
				main.withdraw()
				if int(checks[1].get()) == 1:
					new.append(author.get(1.0, END).strip())
				else:
					new.append(originals[1])
				if int(checks[3].get()) == 1:
					new.append(style.get(1.0, END).strip())
				else:
					new.append(originals[2])
				if int(checks[4].get()) == 1:
					new.append(description.get(1.0, END).strip())
				else:
					new.append(originals[3])

				new_file_name = new[0]
				new_file_save = new_file_name
				x = ''
				while os.path.isfile(f'PRESETS_HERE/{new_file_name}.vital'):
					new_file_name = new_file_save + x
					x += '0'

				change_data = jh.open_file(f'PRESETS_HERE/{originals[0]}.vital')
				change_data['preset_name'], change_data['author'], change_data['preset_style'], change_data['comments'] = new_file_name, new[1], new[2], new[3]
				jh.write_file(f'PRESETS_HERE/{originals[0]}.vital', change_data)

				new_location = f'PRESETS_HERE/{new_file_name}.vital'
				os.rename(f'PRESETS_HERE/{originals[0]}.vital', new_location)

			else:
				illegal = 'yes'
				Label(out_frame, text = "Please make sure your name doesn't have any characters not listed here:\n0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_- ", bg = d_bg, fg = fg).grid(row = 7, columnspan = 5)
		if illegal == 'no':
			main.destroy()




	def exit_main():
		global end_it_all
		end_it_all = 'yes'
		main.destroy()

	Button(main, text = 'Exit', command = exit_main) .grid(row = 4, column = 1, sticky = NSEW, pady = 10)
	Button(main, text = 'APPLY TO SELECTED', command = apply_data, bg = text, relief = FLAT) .grid(row = 4, column = 0, sticky = EW, padx = 10, pady = 10)
	Button(main, image = options_icon, command = settings_edit) .grid(row = 4, column = 2, padx = 3)

	def preview_changes_event(event):
		start()
		try:
			preview_text = preview_changes()
			preview.config(text = preview_text[0])
		except Exception:
			pass
		end()

	main.bind('<Button-1>', preview_changes_event)
	# Open error menu
	def error_menu(problems):
		error = Toplevel()
		error.title('Errors')

		Label(error, text = 'The following preset were unable to load, please check that they have the necessary information') .pack()
		for x in problems:
			Label(error, text = x) .pack()

		def exit():
			error.destroy()

		Button(error, text = "EXIT", command = exit) .pack()

		error.mainloop()

	if len(problems) != 0:
		error_menu(problems)

	main.mainloop()

while True:
	if end_it_all == 'no':
		gui()
		if end_it_all == 'yes':
			break
	else:
		pass