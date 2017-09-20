"""
hello.py: Quoting from "Cygnus X-1 Book Two: Hemispheres.
"""

# System and third-party imports.
import logging
import optparse

# Constants.
EXT_SUCCESS = 0x0000
EXT_WRONG_SECTION = 0x0001

SECTION_TITLES = ['prelude',
                  'apollo: bringer of wisdom',
                  'dionysus: bringer of love',
                  'armageddon: the battle of heart and mind',
                  'cygnus: bringer of balance',
                  'the sphere: a kind of dream'
                  ]

SECTION_LYRICS = {
    SECTION_TITLES[0]: 'When our weary world was young\n'
                       'The struggle of the ancients first began\n'
                       'The gods of Love and Reason\n'
                       'Sought alone to rule the fate of Man\n'
                       '\n'
                       'They battled through the ages\n'
                       'But still neither force would yield\n'
                       'The people were divided,\n'
                       'Every soul a battlefield\n',
    SECTION_TITLES[1]: 'I bring truth and understanding,\n'
                       'I bring wit and wisdom fair,\n'
                       'Precious gifts beyond compare.\n'
                       'We can build a world of wonder,\n'
                       'I can make you all aware\n'
                       '\n'
                       'I will find you food and shelter,\n'
                       'Show you fire to keep you warm\n'
                       'Through the endless winter storm.\n'
                       'You can live in grace and comfort\n'
                       'In the world that you transform\n'
                       '\n'
                       'The people were delighted\n'
                       'Coming forth to claim their prize\n'
                       'They ran to build their cities\n'
                       'And converse among the wise\n'
                       '\n'
                       'But one day the streets fell silent\n'
                       'Yet they knew not what was wrong\n'
                       'The urge to build these fine things\n'
                       'Seemed not to be so strong\n'
                       '\n'
                       'The wise men were consulted\n'
                       'And the Bridge of Death was crossed\n'
                       'In quest of Dionysus\n'
                       'To find out what they had lost\n',
    SECTION_TITLES[2]: 'I bring love to give you solace\n'
                       'In the darkness of the night\n'
                       'In the Heart\'s eternal light\n'
                       'You need only trust your feelings\n'
                       'Only Love can steer you right\n'
                       '\n'
                       'I bring laughter, I bring Music,\n'
                       'I bring joy and I bring Tears\n'
                       'I will soothe your primal fears\n'
                       'Throw off those chains of Reason\n'
                       'And your prison disappears\n'
                       '\n'
                       'The cities were abandoned\n'
                       'And the forests echoed song\n'
                       'They danced and lived as brothers\n'
                       'They knew Love could not be wrong\n'
                       '\n'
                       'Food and wine they had aplenty\n'
                       'And they slept beneath the stars\n'
                       'The people were contented\n'
                       'And the Gods watched from afar\n'
                       '\n'
                       'But the winter fell upon them\n'
                       'And it caught them unprepared\n'
                       'Bringing wolves and cold starvation\n'
                       'And the hearts of men despaired\n',
    SECTION_TITLES[3]: 'The Universe divided\n'
                       'As the Heart and Mind collided\n'
                       'With the people left unguided\n'
                       'For so many troubled years\n'
                       'In a cloud of doubts and fears\n'
                       'Their world was torn asunder into hollow hemispheres\n'
                       '\n'
                       'Some fought themselves, some fought each other\n'
                       'Most just followed one another\n'
                       'Lost and aimless like their brothers\n'
                       'For their hearts were so unclear\n'
                       'And the truth could not appear\n'
                       'Their spirits were divided into blinded hemispheres\n'
                       '\n'
                       'Some who did not fight\n'
                       'Brought tales of old to light\n'
                       'My Rocinante sailed by night\n'
                       'On her final flight\n'
                       '\n'
                       'To the heart of Cygnus\' fearsome force\n'
                       'We set our course.\n'
                       'Spiralled through that timeless space\n'
                       'To this immortal place\n',
    SECTION_TITLES[4]: 'I have memory and awareness\n'
                       'But I have no shape or form\n'
                       'As a disembodied spirit\n'
                       'I am dead and yet unborn\n'
                       '\n'
                       'I have passed into Olympus\n'
                       'As was told in tales of old\n'
                       'To the City of Immortals\n'
                       'Marble white and purest gold\n'
                       '\n'
                       'I see the Gods in battle rage on high\n'
                       'Thunderbolts across the sky\n'
                       'I cannot move, I cannot hide\n'
                       'I feel a silent scream begin inside\n'
                       '\n'
                       'Then all at once the chaos ceased\n'
                       'A stillness fell, a sudden peace\n'
                       'The Warriors felt my silent cry\n'
                       'And stayed their struggle, mystified\n'
                       '\n'
                       'Apollo was astonished\n'
                       'Dionysus thought me mad\n'
                       'But they heard my story further\n'
                       'And they wondered, and were sad\n'
                       '\n'
                       'Looking down from Olympus\n'
                       'On a world of doubt and fear\n'
                       'Its surface splintered into\n'
                       'Sorry hemispheres.\n'
                       '\n'
                       'They sat a while in silence\n'
                       'Then they turned at last to me\n'
                       'We will call you Cygnus\n'
                       'The God of Balance you shall be\n',
    SECTION_TITLES[5]: 'We can walk our road together\n'
                       'If our goals are all the same\n'
                       'We can run alone and free\n'
                       'If we pursue a different aim\n'
                       '\n'
                       'Let the truth of Love be lighted\n'
                       'Let the love of truth shine clear\n'
                       'Sensibility\n'
                       'Armed with sense and liberty\n'
                       'With the Heart and Mind united\n'
                       'In a single perfect sphere\n'
}


def main(section):
    if (section not in SECTION_TITLES):
        logging.info('Unknown section forwarded.')
        raise SystemExit(EXT_WRONG_SECTION)

    print '--------------------------------'
    print 'CYGNUS X-1 BOOK TWO: HEMISPHERES'
    print 'Section: {section}'.format(section=section.title())
    print '--------------------------------'
    print ''
    print SECTION_LYRICS[section]


if (__name__ == '__main__'):
    logging.getLogger().setLevel(logging.INFO)

    parser = optparse.OptionParser()
    parser.add_option('--section',
                      default='prelude',
                      help='Song sections: prelude | apollo: bringer of wisdom | dionysus: bringer of love | '
                           'armageddon: the battle of heart and mind | cygnus: bringer of balance | '
                           'the sphere: a kind of dream')

    (options, args) = parser.parse_args()

    main(options.section)

    raise SystemExit(EXT_SUCCESS)
