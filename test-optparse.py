import optparse


parser = optparse.OptionParser()
parser.add_option('-t', '--trace', action='store_true', dest='trace',
                  help="print out trace info.",
                  metavar='<trace>')

parser.add_option('command',  action='store', dest='command',
                  help="subcommands",
                  metavar='<>')

opt, args = parser.parse_args()

print opt.trace
print args
