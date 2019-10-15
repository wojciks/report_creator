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
            LOCATION        VARCHAR(50)     NOT NULL,
            TIMELOCAL       INTEGER         NOT NULL, 
            TZ              INTEGER         NOT NULL,
            TIMEUTC         INTEGER,
            TIMEFROMLAST    INTEGER,
            LAT             CHARACTER(8)    NOT NULL,
            LON             CHARACTER(9)    NOT NULL,
            COURSE          INTEGER,
            GPSDIST         REAL,
            GPSAVGSPD       REAL,
            VOYDIST         INTEGER,
            VOYTIME         INTEGER,
            REMAININGDIST   REAL,
            VOYGPSAVGSPD    REAL,
            LOGFROMLAST     REAL,
            LOGSPDLAST      REAL,
            CURRENTSPD      REAL,
            
            POBTIMELOCAL    INTEGER,
            POFFTIMELOCAL   INTEGER,
            
            NEXTPORT        VARCHAR(50),
            ETATIMELOCAL    INTEGER,   
            ETATZ           INTEGER,
            ETATIMEUTC      INTEGER, 
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
            ETCLOCAL            INTEGER,
            ETCUTC              INTEGER,
            ETDLOCAL            INTEGER,
            ETDUTC              INTEGER)''')
    c = conn.cursor()
    key_string = str(list(data_dictionary.keys())).replace('~','').replace('[','').replace(']','').replace("'", "")
    value_string = str(list(data_dictionary.values())).replace('[','').replace(']','')
    c.execute(f'INSERT INTO VOYAGE_EVENT ({key_string}) VALUES ({value_string});')
    conn.commit()
    return conn


def voyage_distance_time_avg_speed(conn, voyage_no):
    c = conn.cursor()
    c.execute(f'SELECT SUM(GPSDIST) FROM VOYAGE_EVENT WHERE VOY = {voyage_no} and (EVENT = "NOONS" or EVENT = "EOSP")')
    voy_dist = float(c.fetchone()[0])
    c.execute(f'SELECT SUM(TIMEFROMLAST) FROM VOYAGE_EVENT WHERE VOY = {voyage_no} and (EVENT = "NOONS" or EVENT = "EOSP")')
    voy_time = float(c.fetchone()[0])
    voy_speed = voy_dist / voy_time
    return {'~VOYDIST~': voy_dist,
            '~VOYTIME~': voy_time,
            '~VOYGPSAVGSPD~': voy_speed}


def last_event_data():
    conn = sqlite3.connect('data_history.db')
    c = conn.cursor()
    c.execute('SELECT VOY, EVENT, TZ, TIMEUTC, REMAININGDIST FROM VOYAGE_EVENT ORDER BY ID DESC limit 1')
    return c.fetchone()
