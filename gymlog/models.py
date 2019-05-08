from django.db import models

class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        self.blank, self.isnull = blank, null
        self.null = True #

    def db_type(self, connection):
        typ=['TIMESTAMP']
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        else:
            return models.DateTimeField.to_python(self, value)

#    def get_db_prep_value(self, value, connection, prepared=False):
#        if value==None:
#            return None
#        return startime('%Y-%m-%d %H:%M:%S',value.timetuple())

# Create your models here.

class gymlog(models.Model):
    exitlog = UnixTimestampField(auto_created=True)
    entrylog = UnixTimestampField(auto_created=True)
    sid =  models.ForeignKey('Student.Student',on_delete=models.CASCADE)
    def __str__(self):
        return str(self.sid) + " : " + str(self.entrylog)
