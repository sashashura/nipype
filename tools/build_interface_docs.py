#!/usr/bin/env python
"""Script to auto-generate interface docs.
"""
# stdlib imports
import os
import sys

#*****************************************************************************
if __name__ == '__main__':
    nipypepath = os.path.abspath('..')
    sys.path.insert(1,nipypepath)
    # local imports
    from interfacedocgen import InterfaceHelpWriter
    package = 'nipype'
    outdir = os.path.join('interfaces','generated')
    docwriter = InterfaceHelpWriter(package)
    # Packages that should not be included in generated API docs.
    docwriter.package_skip_patterns += ['\.externals$',
                                        '\.utils$',
                                        '\.pipeline',
                                        '.\testing',
                                        ]
    # Modules that should not be included in generated API docs.
    docwriter.module_skip_patterns += ['\.version$',
                                       '\.interfaces\.afni$',
                                       '\.interfaces\.base$',
                                       '\.interfaces\.matlab$',
                                       '\.interfaces\.rest$',
                                       '\.interfaces\.pymvpa$',
                                       '\.interfaces\.traits',
                                       '\.pipeline\.alloy$',
                                       '\.pipeline\.s3_node_wrapper$',
                                       '.\testing',
                                       ]
    docwriter.class_skip_patterns += ['FSL',
                                      'FS',
                                      'Spm',
                                      'Tester',
                                      'Spec$',
                                      'afni',
                                      'Numpy'
                                      ]
    docwriter.write_api_docs(outdir)
    docwriter.write_index(outdir, 'gen', relative_to='interfaces')
    print '%d files written' % len(docwriter.written_modules)
