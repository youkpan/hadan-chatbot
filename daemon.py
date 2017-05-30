from chatbot import chatbot
chatbot2 = chatbot.Chatbot()
chatbot2.main({'--test=daemon'})
#.main(['--modelTag', 'server', '--test', 'daemon', '--rootDir', chatbotPath])
chatbot2.daemonPredict('你好')
