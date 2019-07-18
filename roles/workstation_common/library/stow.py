#!/usr/bin/python

DOCUMENTATION = '''
---
module: stow

short_description: Manage files using GNU Stow

version_added: "2.4"

options:
    name:
        description:
            - The name of the item to be stowed
        required: true
    source:
	description:
	    - The source of your stowed files
	required: true
    target:
	description:
	    - The directory where youre stow links will be placed
	default: $HOME
    overwrite_conflicts:
	description:
	    - Whether Stow should delete any existing files in the target, when
 	      encountering conflicts linking the source to the target
	default: false

author:
    - Matt Valentine-House (@eightbitraptor)
'''

EXAMPLES = '''
# stow my bash files overwriting any that already exist
- name: Stow bash
  stow:
    name: bash
    source: /home/user/.dotfiles
    overwrite_conflicts: yes

'''

import re
import os

from ansible.module_utils.basic import AnsibleModule

def detect_conflicting_files(message, base_dir):
    conflict_file_matcher = re.compile(
        "existing target is neither a link nor a directory: (\.?\w+)"
    )
    conflict_files = conflict_file_matcher.findall(message)

    return [
        os.path.join(base_dir, fname) for fname in conflict_files
    ]


def run_module():
    module_args = dict(
        name                = dict(type='str',  required=True),
        source              = dict(type='str',  required=True),
        target              = dict(type='str',  required=False),
        overwrite_conflicts = dict(type='bool', required=False, default=False)
    )

    result = dict(
        changed=False,
        message=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(msg="skipped, running in check mode", skipped=True)

    name                = module.params['name']
    source              = module.params['source']
    target              = module.params['target'] or os.getenv('HOME')
    overwrite_conflicts = module.params['overwrite_conflicts']

    command = "stow --verbose=1 --dir={}".format(source)

    rc, out, err = module.run_command(
        "{} -t {} {}".format(command, target, name)
    )

    if rc == 0:
        if err:
            result['message'] = "Stowed {}".format(name)
            result['changed'] = True
        else:
            result['message'] = "No updates required"
            result['changed'] = False
    else:
        conflicts = detect_conflicting_files(err, target)

        if overwrite_conflicts:
            for fpath in conflicts:
                os.remove(fpath)
                rc, out, err = module.run_command(
                    "{} -t {} {}".format(command, target, name)
                )
        else:
            conflict_error = (
                "File Conflict Error for files {}. "
                "If you intended these file to be managed by Stow, set "
                "overwrite_conflicts: yes in your Playbook"
            ).format(conflicts)

            module.fail_json(msg=conflict_error, **result)

    module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
