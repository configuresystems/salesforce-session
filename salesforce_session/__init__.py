from simple_salesforce import Salesforce
import json
import marshal
import os


class SalesForceSession(Salesforce):
    def __init__(self):
        self.session = self.__create_session()

    def __set_credentials(self):
        _credentials = dict(
                username=os.environ['SF_USERNAME'],
                password=os.environ['SF_PASSWORD'],
                security_token=os.environ['SF_SECURITY_TOKEN'],
                client_id=os.environ['SF_CLIENT_ID']
                )
        return _credentials

    def __convert_to_json(self, object_data):
        return json.loads(json.dumps(object_data))

    def __create_session(self):
        _credentials = self.__set_credentials()
        session = Salesforce(
                **_credentials
                )
        return session

    def __build_fields(self, field_list=[]):
        if isinstance(field_list, list):
            fields = (',').join(field_list)
        return self.query_prep.append(fields)

    def __build_query_type(self, query_type='SELECT'):
        return self.query_prep.append(query_type)

    def __build_conditions(self, conditions=None):
        if conditions:
            return self.query_prep.append('WHERE {0}'.format(conditions))

    def __build_object(self, sql_object=None):
        if sql_object:
            return self.query_prep.append('FROM {0}'.format(sql_object))

    def __build_limit(self, limit=None):
        if limit and isinstance(limit, int):
            return self.query_prep.append('LIMIT {0}'.format(limit))

    def __build_query(self, query_type, fields, sql_object, conditions, limit):
        self.query_prep = []
        if not query_type:
            query_type = 'SELECT'
        self.__build_query_type(query_type)
        self.__build_fields(fields)
        self.__build_object(sql_object)
        self.__build_conditions(conditions)
        self.__build_limit(limit)
        statement = (' ').join(self.query_prep)
        return statement


    def query(self, query_type, fields, sql_object, conditions=None, limit=None):
        query = self.__build_query(query_type,fields,sql_object,conditions,limit)
        return self.__convert_to_json(self.session.query_all(query)['records'])

    def raw_query(self, query):
        return self.session.query_all(query)['records']

    def get_session(self):
        if not self.session:
            self.session = self.__create_session()
        return self.session
