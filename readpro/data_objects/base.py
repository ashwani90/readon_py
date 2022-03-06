import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class Base:
    def create_fields(self,data):
        fields = {}
        try:
            for i in self.all_fields:
                fields[i] = data[i]
            for j in self.optional_fields:
                if j in data:
                    fields[j] = data[j]
            return fields
        except Exception as e:
            logger.error("Error Creating the data %s" % e)
            return None
        
    def check_update_fields(self,data):
        fields = {}
        try:
            for i in self.all_fields:
                if i in data:
                    fields[i] = data[i]
            for j in self.optional_fields:
                if j in data:
                    fields[j] = data[j]
            return fields
        except Exception as e:
            logger.error("Error Creating the data %s" % e)
            return None
        
    def check_where_clause(self,data):
        return self.check_update_fields(data)