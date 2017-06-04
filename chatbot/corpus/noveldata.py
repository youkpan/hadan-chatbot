#coding:utf-8
# Copyright 2015 Conchylicultor. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import os
import random
from tqdm import tqdm

"""
Ubuntu Dialogue Corpus

http://arxiv.org/abs/1506.08909

"""

class NovelData:
    """
    """

    def __init__(self, dirName):
        """
        Args:
            dirName (string): directory where to load the corpus
        """
        self.MAX_NUMBER_SUBDIR = 10
        self.conversations = []
        __dir = os.path.join(dirName, "Novel")
        number_subdir = 0
        for sub in tqdm(os.scandir(__dir), desc="Ubuntu dialogs subfolders", total=len(os.listdir(__dir))):
            if number_subdir == self.MAX_NUMBER_SUBDIR:
                print("WARNING: Early stoping, only extracting {} directories".format(self.MAX_NUMBER_SUBDIR))
                return

            if sub.is_dir():
                number_subdir += 1
                for f in os.scandir(sub.path):
                        self.conversations.append({"lines": self.loadLines(f.path)})


    def loadLines(self, fileName):
        """
        Args:
            fileName (str): file to load
        Return:
            list<dict<str>>: the extracted fields for each line
        """
        lines = []
        with open(fileName, "rb") as f:
          #if(f.readline() == ""):
          print("geting data")
          bookdata = f.read(190*1000000).decode('GBK','ignore')
          print("geting data  OK ")
          lineu = bookdata

        text_words = len(bookdata)
        #for line in f.readlines():
        position = 0
        last_position = 0
        append_cnt = 0
        while(position+500 < text_words):

              while(position +100 < text_words ):
                word_s = str(lineu[position])#.encode('utf-8')
                #print(word_s)
                if( word_s ==u"：" or word_s ==u":"  or word_s ==u"「"  or word_s==u"“" or word_s==u'"' ):
                    #print('new1----------------------------------',word_s)
                    break
                position +=1

              position +=1
              for k in range(position,position+ 6):
              	word_s = str(lineu[k]) #.encode('utf-8')
              	#print('check',word_s)
              	if   word_s==u"，" or word_s==u"“" or  word_s==u"”" or word_s==u"「"  or word_s==u"」"  or word_s==u"　" or word_s==u'\u3000'  or  word_s==u" " or  word_s==u' '  or word_s==u"'" or  word_s==u'"' or  word_s==u"\r" or  word_s==u"\n":
                	#print('new2----------------------------------',word_s)
                	position +=1
                	#print('skip',word_s)
              	else:
                  break

              #else:
                #position +=1
              word_s = str(lineu[position])
              #print(word_s)
              position +=1
              #lineu=line.decode('utf-8')
              line_vector = []
              #line_mark = np.ones(sentence_len)
              #print(line)
              position_t =  position
              position_start = position
              #print("----------")
              sentence = ''
              sentence1 = ''
              findnewline = False
              for k in range(position,position+ 20*2):
                try:
                  #print( word_s,dict_index[word_s] )
                  sentence += word_s
                  #word_v = dict_vector[dict_index[word_s]]
                  word_s = str(lineu[k])

                  if((( word_s ==u'，') and (position_t-position >7)) or
                    word_s ==u'。' or word_s ==u'；' or word_s ==u'！' or word_s ==u'？' or word_s ==u'”' or word_s ==u'」'
                    or word_s =='.' or word_s ==';' or word_s =='!' or word_s =='?' or word_s =='"' ):
                      #print('new3----------------------------------',word_s)
                      position_t +=1
                      sentence1 = sentence #not use the end word
                      sentence += word_s
                      break
                  if(word_s == u"\r" or word_s == u"\n"):
                      findnewline = True
                      break
                  position_t +=1

                except Exception as e:
                  pass

              position = position_t
              #if findnewline:
                #  print('find new line-----------')
              if len(sentence)< 4  or findnewline:
                continue

              if( position_start - last_position < 50 and last_position>0):
                 lines.append({"text": last_sentence})
                 lines.append({"text": sentence})
                 #print(append_cnt,"  ---------- :")
                 #print (last_position,last_sentence)
                 #print (position_start,sentence)

              last_position = position
              if(random.random()*100 < 90):
                last_sentence = sentence1
              else:
                last_sentence = sentence

              lline=len(lines)
              if( lline%10000 <20  ):
               print (len(lines),sentence,len(sentence))

              append_cnt +=1
        print('len lines',len(lines))
        return lines


    def getConversations(self):
        return self.conversations
