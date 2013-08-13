# argparse is suggested, optparse is deprecated.
import argparse


def delete(args):
    print 'delete %s' % args.id


def create(args):
    print 'Create %s' % args.id


parser = argparse.ArgumentParser()

# Setup base arguments
parser.add_argument('command', help='subcommand to run.', metavar='<command>',
                    nargs='?')
parser.add_argument('-v', '--verbose',
                    help='verbose', type=int,
                    choices=[0, 1, 2])
parser.add_argument('-t', '--trace',
                    action='count',
                    dest='trace')

# setup subcommands
subparsers = parser.add_subparsers(title='subcommands',
                            description='Some commands you can use in nova',
                            help='choise you subcommand')

parser_create = subparsers.add_parser('create', help="create nova")
parser_create.add_argument('--id', action='store', dest='id')
parser_create.set_defaults(func=create)

parser_delete = subparsers.add_parser('delete', help="delete nova")
parser_delete.add_argument('--id', action='store', dest='id')
parser_delete.set_defaults(func=delete)

# parse_args()
args = parser.parse_args()
args.func(args)
