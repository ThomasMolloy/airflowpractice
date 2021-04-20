from sqlalchemy import create_engine
import pandas as pd
import configparser

def generate_DB():
    '''
    Read json file into pandas dataframe and perform some preprocessing to prepare data
    before inserting into mysql datbase
    '''
    fighter_df = pd.read_json('data/FighterData_2021-04-18.json')
    temp_df = pd.DataFrame.from_dict((fighter_df['CareerStats'].to_dict())).T
    fighter_df.drop(columns=['CareerStats'], inplace=True)
    temp_df.drop(columns=['FirstName','LastName'], inplace=True)
    fighter_df = pd.merge(fighter_df,temp_df,on='FighterId')

    '''
    Obtain mysql database information and create/insert fighter info dataframe into table
    '''
    cfg = configparser.ConfigParser()
    cfg.read('mmadata.cfg')
    host = cfg['mysql']['host']
    user = cfg['mysql']['user']
    passwd = cfg['mysql']['passwd']
    port = cfg['mysql']['port']
    dbname = cfg['mysql']['dbname']
    
    engine = create_engine(f'mysql+mysqlconnector://{user}:{passwd}@{host}:{port}/{dbname}')
    fighter_df.to_sql(name='Fighter_Info', con=engine, if_exists='replace')

if __name__ == '__main__':
    generate_DB()