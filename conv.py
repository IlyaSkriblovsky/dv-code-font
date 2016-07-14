#!/usr/bin/env python

import fontforge

config = {
    'source_ttf': 'DejaVuSansMono.ttf',

    'firacode_ttf': 'FiraCode-Regular.otf',

    'output': {
        'filename': 'DVCode.ttf',
        'fontname': 'DVCode',
        'fullname': 'DV Code',
        'familyname': 'DV Code',
        'copyright_add': '\nProgramming ligatures added by Ilya Skriblovsky from FiraCode\nFiraCode Copyright (c) 2015 by Nikita Prokopov',
        'unique_id': 'DV Code',
    },

    'add_ligatures': [
        {   # <-
            'chars': ['less', 'hyphen'],
            'firacode_ligature_name': 'less_hyphen.liga',
        },
        {   # <--
            'chars': ['less', 'hyphen', 'hyphen'],
            'firacode_ligature_name': 'less_hyphen_hyphen.liga',
        },
        {   # ->
            'chars': ['hyphen', 'greater'],
            'firacode_ligature_name': 'hyphen_greater.liga',
        },
        {   # -->
            'chars': ['hyphen', 'hyphen', 'greater'],
            'firacode_ligature_name': 'hyphen_hyphen_greater.liga',
        },
        {   # <>
            'chars': ['less', 'greater'],
            'firacode_ligature_name': 'less_greater.liga',
        },
        {   # <->
            'chars': ['less', 'hyphen', 'greater'],
            'firacode_ligature_name': 'less_hyphen_greater.liga',
        },
        {   # =>
            'chars': ['equal', 'greater'],
            'firacode_ligature_name': 'equal_greater.liga',
        },
        {   # ==>
            'chars': ['equal', 'equal', 'greater'],
            'firacode_ligature_name': 'equal_equal_greater.liga',
        },
        {   # <==
            'chars': ['less', 'equal', 'equal'],
            'firacode_ligature_name': 'less_equal_equal.liga',
        },
        {   # ?=
            'chars': ['question', 'equal'],
            'firacode_ligature_name': 'question_equal.liga',
        },
        {   # !=
            'chars': ['exclam', 'equal'],
            'firacode_ligature_name': 'exclam_equal.liga',
        },
        {   # ==
            'chars': ['equal', 'equal'],
            'firacode_ligature_name': 'equal_equal.liga',
        },
        {   # <=
            'chars': ['less', 'equal'],
            'firacode_ligature_name': 'equal_less.liga',
        },
        {   # >=
            'chars': ['greater', 'equal'],
            'firacode_ligature_name': 'greater_equal.liga',
        },
        {   # ::
            'chars': ['colon', 'colon'],
            'firacode_ligature_name': 'colon_colon.liga',
        },
        {   # ===
            'chars': ['equal', 'equal', 'equal'],
            'firacode_ligature_name': 'equal_equal_equal.liga',
        },
        {   # !==
            'chars': ['exclam', 'equal', 'equal'],
            'firacode_ligature_name': 'exclam_equal_equal.liga',
        },
        {   # ??
            'chars': ['question', 'question'],
            'firacode_ligature_name': 'question_question.liga',
        },
        {   # !!
            'chars': ['exclam', 'exclam'],
            'firacode_ligature_name': 'exclam_exclam.liga',
        },
        {   # --
            'chars': ['hyphen', 'hyphen'],
            'firacode_ligature_name': 'hyphen_hyphen.liga',
        },
        {   # ---
            'chars': ['hyphen', 'hyphen', 'hyphen'],
            'firacode_ligature_name': 'hyphen_hyphen_hyphen.liga',
        },
        {   # /*
            'chars': ['slash', 'asterisk'],
            'firacode_ligature_name': 'slash_asterisk.liga',
        },
        {   # /**
            'chars': ['slash', 'asterisk', 'asterisk'],
            'firacode_ligature_name': 'slash_asterisk_asterisk.liga',
        },
        {   # */
            'chars': ['asterisk', 'slash'],
            'firacode_ligature_name': 'asterisk_slash.liga',
        },
        {   # //
            'chars': ['slash', 'slash'],
            'firacode_ligature_name': 'slash_slash.liga',
        },
        {   # ///
            'chars': ['slash', 'slash', 'slash'],
            'firacode_ligature_name': 'slash_slash_slash.liga',
        },
        {   # ||
            'chars': ['bar', 'bar'],
            'firacode_ligature_name': 'bar_bar.liga',
        },
        {   # ||=
            'chars': ['bar', 'bar', 'equal'],
            'firacode_ligature_name': 'bar_bar_equal.liga',
        },
        {   # |=
            'chars': ['bar', 'equal'],
            'firacode_ligature_name': 'bar_equal.liga',
        },
        {   # ^=
            'chars': ['asciicircum', 'equal'],
            'firacode_ligature_name': 'asciicircum_equal.liga',
        },
        {   # ~=
            'chars': ['asciitilde', 'equal'],
            'firacode_ligature_name': 'asciitilde_equal.liga',
        },
        {   # =~
            'chars': ['equal', 'asciitilde'],
            'firacode_ligature_name': 'equal_asciitilde.liga',
        },
        {   # ~>
            'chars': ['asciitilde', 'greater'],
            'firacode_ligature_name': 'asciitilde_greater.liga',
        },
        {   # ~~>
            'chars': ['asciitilde', 'asciitilde', 'greater'],
            'firacode_ligature_name': 'asciitilde_asciitilde_greater.liga',
        },
        {   # <<
            'chars': ['less', 'less'],
            'firacode_ligature_name': 'less_less.liga',
        },
        {   # >>
            'chars': ['greater', 'greater'],
            'firacode_ligature_name': 'greater_greater.liga',
        },
    ]
}



class LigatureCreator(object):

    def __init__(self, font, firacode):
        self.font = font
        self.firacode = firacode

        self._lig_counter = 0

    def add_ligature(self, input_chars, firacode_ligature_name):
        self._lig_counter += 1

        ligature_name = 'lig.{}'.format(self._lig_counter)

        self.font.createChar(-1, ligature_name)
        firacode.selection.none()
        firacode.selection.select(firacode_ligature_name)
        firacode.copy()
        self.font.selection.none()
        self.font.selection.select(ligature_name)
        self.font.paste()


        self.font.selection.none()
        self.font.selection.select('space')
        self.font.copy()

        lookup_name = lambda i: 'lookup.{}.{}'.format(self._lig_counter, i)
        lookup_sub_name = lambda i: 'lookup.sub.{}.{}'.format(self._lig_counter, i)
        cr_name = lambda i: 'CR.{}.{}'.format(self._lig_counter, i)

        for i, char in enumerate(input_chars):
            self.font.addLookup(lookup_name(i), 'gsub_single', (), ())
            self.font.addLookupSubtable(lookup_name(i), lookup_sub_name(i))

            if i < len(input_chars) - 1:
                self.font.createChar(-1, cr_name(i))
                self.font.selection.none()
                self.font.selection.select(cr_name(i))
                self.font.paste()

                self.font[char].addPosSub(lookup_sub_name(i), cr_name(i))
            else:
                self.font[char].addPosSub(lookup_sub_name(i), ligature_name)


        calt_lookup_name = 'calt.{}'.format(self._lig_counter)
        self.font.addLookup(calt_lookup_name, 'gsub_contextchain', (), (('calt', (('DFLT', ('dflt',)), ('arab', ('dflt',)), ('armn', ('dflt',)), ('cyrl', ('SRB ', 'dflt')), ('geor', ('dflt',)), ('grek', ('dflt',)), ('lao ', ('dflt',)), ('latn', ('CAT ', 'ESP ', 'GAL ', 'ISM ', 'KSM ', 'LSM ', 'MOL ', 'NSM ', 'ROM ', 'SKS ', 'SSM ', 'dflt')), ('math', ('dflt',)), ('thai', ('dflt',)))),))
        for i, char in enumerate(input_chars):
            ctx_subtable_name = 'calt.{}.{}'.format(self._lig_counter, i)
            ctx_spec = '{prev} | {cur} @<{lookup}> | {next}'.format(
                prev = ' '.join(cr_name(j) for j in range(i)),
                cur = char,
                lookup = lookup_name(i),
                next = ' '.join(input_chars[i+1:]),
            )
            self.font.addContextualSubtable(calt_lookup_name, ctx_subtable_name, 'glyph', ctx_spec)


def change_font_names(font, fontname, fullname, familyname, copyright_add, unique_id):
    font.fontname = fontname
    font.fullname = fullname
    font.familyname = familyname
    font.copyright += copyright_add
    font.sfnt_names = tuple(
        (row[0], 'UniqueID', unique_id) if row[1] == 'UniqueID' else row
        for row in font.sfnt_names
    )


font = fontforge.open(config['source_ttf'])
firacode = fontforge.open(config['firacode_ttf'])
firacode.em = font.em

creator = LigatureCreator(font, firacode)
ligature_length = lambda lig: len(lig['chars'])
for lig_spec in sorted(config['add_ligatures'], key = ligature_length):
    try:
        creator.add_ligature(lig_spec['chars'], lig_spec['firacode_ligature_name'])
    except Exception as e:
        print('Exception while adding ligature: {}'.format(lig_spec))
        raise

change_font_names(font, config['output']['fontname'],
                        config['output']['fullname'],
                        config['output']['familyname'],
                        config['output']['copyright_add'],
                        config['output']['unique_id'])

font.generate(config['output']['filename'])
