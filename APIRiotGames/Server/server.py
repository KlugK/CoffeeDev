from autobahn.twisted.websocket import WebSocketServerProtocol, WebSocketServerFactory
import lolApi as l
import json 

class MyServerProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if not isBinary:
            summonerName = payload.decode('utf8')
            print("Summoner Name received: {0}".format(summonerName))
            summonerId = l.get_summoner_id(summonerName)
            summonerIdJson = json.dumps(summonerId)
            self.sendMessage(summonerIdJson.encode("utf-8"))

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))


if __name__ == '__main__':

    import sys

    from twisted.python import log
    from twisted.internet import reactor

    log.startLogging(sys.stdout)

    factory = WebSocketServerFactory(u"ws://127.0.0.1:9000")
    factory.protocol = MyServerProtocol

    reactor.listenTCP(9000, factory)
    reactor.run()