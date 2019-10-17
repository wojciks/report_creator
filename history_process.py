import sqlite3
import os


def check_and_update_database(data_dictionary):
    if os.path.isfile('data_history.db'):
        conn = sqlite3.connect('data_history.db')
    else:
        conn = sqlite3.connect('data_history.db')
        conn.execute('''
        CREATE TABLE VOYAGE_EVENT(
            ID              INTEGER         PRIMARY KEY,
            VOY             VARCHAR(10)     NOT NULL,
            EVENT           VARCHAR(10)     NOT NULL,
            LOCATION        VARCHAR(50),
            TIMELOCAL       VARCHAR         NOT NULL, 
            TZ              VARCHAR         NOT NULL,
            TIMEUTC         INTEGER,
            TIMEFROMLAST    INTEGER,
            LAT             CHARACTER(8)    NOT NULL,
            LON             CHARACTER(9)    NOT NULL,
            COURSE          INTEGER,
            GPSDIST         REAL,
            GPSAVGSPD       REAL,
            VOYDIST         REAL,
            VOYLOGDIST      REAL,
            VOYTIME         INTEGER,
            REMAININGDIST   REAL,
            VOYGPSAVGSPD    REAL,
            LOGFROMLAST     REAL,
            LOGSPDLAST      REAL,
            CURRENTSPD      REAL,
            
            NEXTPORT        VARCHAR(50),
            ETATIMELOCAL    VARCHAR,   
            ETATZ           REAL,
            ETATIMEUTC      VARCHAR, 
            WINDDIR         VARCHAR(3),
            WINDFORCEKTS    INTEGER,
            WINDFORCEB      INTEGER,
            SEAHEIGHT       INTEGER,
            SEADIR          VARCHAR(3),
            SWELL           REAL,
            AIRTEMP         INTEGER,
            PRESSURE        INTEGER,
            BILGES          VARCHAR(50),
            REMARKS         VARCHAR(150),
            MASTER          VARCHAR(50),
            
            HFOROB              REAL,
            MDOROB              REAL,
            LOCYLROB            REAL,
            LOMEROB             REAL,
            LOAUXROB            REAL,
            LOTOTALROB          REAL,
            FWROB               REAL,
            FWPROD              REAL,
            FWCONS              REAL,
            MEHFOCONS           REAL,
            MEMDOCONS           REAL,
            AUXHFOCONS          REAL,
            AUXMDOCONS          REAL,
            BOILERHFOCONS       REAL,
            BOILERMDOCONS       REAL,
            TOTALHFOCONS        REAL,
            TOTALMDOCONS        REAL,
            LOCYLCONS           REAL,
            LOMECONS            REAL,
            LOAUXCONS           REAL,
            TOTALLOCONS         REAL,
            RPM                 REAL,
            MEDIST              REAL,
            MESPD               REAL,
            SLIP                REAL,
            MEKW                REAL,
            MEKWH               REAL,
            MELOAD              REAL,
            MEGOV               REAL,
            AUXTIME             REAL,
            AUXKW               REAL,
            AUXKWH              REAL,
            SLUDGETK            REAL,
            OILYBILGETK         REAL,
            INCINERATORSETTLINGTK REAL,
            INCINERATORSERVICETK REAL,
            BILGEWATERTK        REAL,
            SLUDGETOTAL         REAL, 
            
            IFCARGO             INTEGER,  
            COMMENCECARGOLOCAL  INTEGER,
            COMMENCECARGOUTC    INTEGER,
            COMPLETEDCARGOLOCAL INTEGER,
            COMPLETEDCARGOUTC   INTEGER,
            CARGOROB            INTEGER,
            CARGODAILY          INTEGER,
            CARGOTOGO           INTEGER,
            BALLASTROB          INTEGER,
            BALLASTDAILY        INTEGER,
            SHORECRANESNO       INTEGER,
            SHIPCRANESNO        INTEGER,
            ETCLOCAL            VARCHAR,
            ETCUTC              VARCHAR,
            ETDLOCAL            VARCHAR,
            ETDUTC              VARCHAR)''')
    c = conn.cursor()
    key_string = str(list(data_dictionary.keys())).replace('~', '').replace('[', '').replace(']', '').replace("'", "")
    value_string = str(list(data_dictionary.values())).replace('[', '').replace(']', '')
    c.execute(f'INSERT INTO VOYAGE_EVENT ({key_string}) VALUES ({value_string});')
    conn.commit()
    return conn


def last_event_data():
    if os.path.isfile('data_history.db'):
        conn = sqlite3.connect('data_history.db')
        c = conn.cursor()
        c.execute(
            'SELECT '
            'VOY, EVENT, TZ, TIMEUTC, REMAININGDIST, VOYTIME, VOYDIST, VOYLOGDIST, NEXTPORT, ETATIMEUTC, ETATZ, MASTER, '
            'REMARKS '
            'FROM VOYAGE_EVENT ORDER BY ID DESC limit 1')
        data = c.fetchone()
        conn.close()
    else:
        data = None
    return data
