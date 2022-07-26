import asyncio
from azure.eventhub.aio import EventHubProducerClient
from azure.eventhub import EventData
from uamqp.constants import TransportType
import json


class statusEvent:
    def __init__(self, name, status, ovdhsp30, ovdhsp60, ovdnav30, ovdnav60, statustimeutc, unitlocked, location, current, baserfs, displaypage, displayfield, shadowpage, shadowfield, brokenmdt, type, tfsplit, notifyflag, activereserve, mutualaid, battalion, division, bureau, baserfsnbr, shopnbr, accessid, homepagenbr, homefieldnbr, gpsbadind, latitude, longitude, azimuth, velocity, utctime, attributes, recordtype, messageid, sendtime, seconds, nanos):
        self.name = name
        self.status = status
        self.ovdhsp30 = ovdhsp30
        self.ovdhsp60 = ovdhsp60
        self.ovdnav30 = ovdnav30
        self.ovdnav60 = ovdnav60
        self.statustimeutc = statustimeutc
        self.unitlocked = unitlocked
        self.location = location
        self.current = current
        self.baserfs = baserfs
        self.displaypage = displaypage
        self.displayfield = displayfield
        self.shadowpage = shadowpage
        self.shadowfield = shadowfield
        self.brokenmdt = brokenmdt
        self.type = type
        self.tfsplit = tfsplit
        self.notifyflag = notifyflag
        self.activereserve = activereserve
        self.mutualaid = mutualaid
        self.battalion = battalion
        self.division = division
        self.bureau = bureau
        self.baserfsnbr = baserfsnbr
        self.shopnbr = shopnbr
        self.accessid = accessid
        self.homepagenbr = homepagenbr
        self.homefieldnbr = homefieldnbr
        self.gpsbadind = gpsbadind
        self.latitude = latitude
        self.longitude = longitude
        self.azimuth = azimuth
        self.velocity = velocity
        self.utctime = utctime
        self.attributes = attributes
        self.recordtype = recordtype
        self.messageid = messageid
        self.sendtime = sendtime
        self.seconds = seconds
        self.nanos = nanos


# def createEvent(firetruck):




async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a connection string to your event hubs namespace and
    # the event hub name.
    # producer = EventHubProducerClient.from_connection_string(conn_str="Endpoint=sb://testevthubnmspc.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=u3lE970I48BEaRaBhXfyvCiUprjvLJ3uRCsuw2gkqf8=", eventhub_name="testevthub1", transport_type=TransportType.AmqpOverWebsocket)
    name = 'event'
    miniLatitude = 33.68390
    maxiLatitude = 33.68402
    minLogitude = -112.1129
    maxLogitude = -112.06950
    incremental = 0.00005
    producer = EventHubProducerClient.from_connection_string(
        # conn_str="Endpoint=sb://testevthubnmspc.servicebus.windows.net/;SharedAccessKeyName=testevthub1shareacpolicy;SharedAccessKey=4sAPFIUEtsf1NgzNy1L6ijzK9vlKXpLvwqEbRYzTs7Y=;EntityPath=testevthub1",
        conn_str="Endpoint=sb://testevthubnmspc.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=u3lE970I48BEaRaBhXfyvCiUprjvLJ3uRCsuw2gkqf8=",
        eventhub_name="testevthub1", transport_type=TransportType.AmqpOverWebsocket)
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        for a in range(2):
          x=str(a)+'_9'
          statusEventOb=statusEvent('Test-'+x,'green'+x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x)
          statusEventStr=json.dumps(statusEventOb.__dict__)
          # statusEventBt=bytes(statusEventStr, 'utf-8')
          statusEventEncode=statusEventStr.encode("UTF-8")
          event_data_batch.add(EventData(statusEventEncode))
        await producer.send_batch(event_data_batch)
        print("123")



        # .add('name', StringType(), False)
        # .add('status', StringType(), True)
        # .add('ovdhsp30', StringType(), True)
        # .add('ovdhsp60', StringType(), True)
        # .add('ovdnav30', StringType(), True)
        # .add('ovdnav60', StringType(), True)
        # .add('statustimeutc', StringType(), True)
        # .add('unitlocked', StringType(), True)
        # .add('location', StringType(), True)
        # .add('current', StringType(), True)
        # .add('baserfs', StringType(), True)
        # .add('displaypage', StringType(), True)
        # .add('displayfield', StringType(), True)
        # .add('shadowpage', StringType(), True)
        # .add('shadowfield', StringType(), True)
        # .add('brokenmdt', StringType(), True)
        # .add('type', StringType(), True)
        # .add('tfsplit', StringType(), True)
        # .add('notifyflag', StringType(), True)
        # .add('activereserve', StringType(), True)
        # .add('mutualaid', StringType(), True)
        # .add('battalion', StringType(), True)
        # .add('division', StringType(), False)
        # .add('bureau', StringType(), True)
        # .add('baserfsnbr', StringType(), True)
        # .add('shopnbr', StringType(), True)
        # .add('accessid', StringType(), True)
        # .add('homepagenbr', StringType(), True)
        # .add('homefieldnbr', StringType(), True)
        # .add('gpsbadind', StringType(), True)
        # .add('latitude', StringType(), True)
        # .add('longitude', StringType(), True)
        # .add('azimuth', StringType(), True)
        # .add('velocity', StringType(), True)
        # .add('utctime', StringType(), True)
        # .add('attributes', StringType(), True)
        # .add('recordtype', StringType(), True)
        # .add('messageid', StringType(), True)
        # .add('sendtime', StringType(), True)
        # .add('seconds', StringType(), True)
        # .add('nanos', StringType(), True)








        # # Add events to the batch.
        # event_data_batch.add(EventData('First event '))
        # # event_data_batch.add(EventData('Second event'))
        # # event_data_batch.add(EventData('Third event'))
        # # Send the batch of events to the event hub.
        # await producer.send_batch(event_data_batch)

loop = asyncio.get_event_loop()
loop.run_until_complete(run())