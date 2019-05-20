from pprint import pprint
import textfsm

template_file = "/home/jdolotko/GIT/pynet_course/Week4/show_ip_bgp.template"
template = open(template_file)

with open("/home/jdolotko/GIT/pynet_course/Week4/show_ip_bgp.txt") as f:
    raw_text_data = f.read()

# Import python debugger to see what is happening
import ipdb
ipdb.set_trace()

# The argument 'template' is a file handle and 'raw_text_data' is a string
re_table = textfsm.TextFSM(template)
data = re_table.ParseText(raw_text_data)

template.close()

print("\nPrint the header row which could be used for dictionary construction")
print(re_table.header)
print("\nOutput Data: ")
pprint(data)
print()

