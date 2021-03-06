#!/usr/bin/env python3

# May you recognize your weaknesses and share your strengths.
# May you share freely, never taking more than you give.
# May you find love and love everyone you find.

import re
import time

import whois

phone_spellable = re.compile(r'^[filoqrsuwxy]+$')

candidate_words = []
with open('/usr/share/dict/words') as f:
    for word in f:
        word = word.strip()
        if phone_spellable.match(word):
            candidate_words.append((len(word), word))

candidate_words.sort()

for word in candidate_words:
    query = False
    while query is False:
        try:
            query = whois.query('%s.com' % word[1])
        except:
            print("Sleeping five seconds...")
            time.sleep(5)
    if not query:
        print(word)
