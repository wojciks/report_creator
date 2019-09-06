import sqlite3
import os
from appconf import USER_DATA_ENTRY_FIELDS


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
            BILGES          VARCHAR(50),
            REMARKS         VARCHAR(150),
            MASTER          VARCHAR(50),
            
            IFLOADING           INTEGER,  
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
    conn.close()

# def avg_spd_calc():
#     conn = sqlite3.connect('data_history.db')
#     c = conn.cursor()
#     c.execute(f'SELECT GPSDIST FROM VOYAGE_EVENT where ID = (SELECT MAX(ID) FROM VOYAGE_EVENT)')
#     dist = c.fetchone()[0]
#     c.execute(f'SELECT TIMEFROMLAST FROM VOYAGE_EVENT where ID = (SELECT MAX(ID) FROM VOYAGE_EVENT)')
#     time = c.fetchone()[0]
#     return dist / time
