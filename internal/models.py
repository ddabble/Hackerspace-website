from datetime import datetime, timedelta
from django.contrib.auth.models import User
from django.db import models


class TimeTable(models.Model):
    slots = models.IntegerField()
    term = models.CharField(max_length=20)

    @classmethod
    def create(cls, slots, term, start_time, per_slot=3):
        table = TimeTable(slots=slots, term=term)
        table.save()
        for slot in range(slots):
            for day in range(5):
                TimeTableSlot.create(start_time + timedelta(hours=2 * slot),
                                     start_time + timedelta(hours=2 * (slot + 1)),
                                     day, table, max_number_of_users=per_slot)

    @staticmethod
    def current_term():
        """
        :return: The current term in the format (yy[HV])
        """
        return str(datetime.now().year)[-2:] + "VH"[datetime.now().month > 6]


class TimeTableSlot(models.Model):
    """
    Time table slot for office hours
    """
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.IntegerField()
    table = models.ForeignKey(TimeTable, on_delete=models.CASCADE)

    @classmethod
    def create(cls, start_time, end_time, day, table, max_number_of_users=3, ):
        slot = TimeTableSlot(start_time=start_time, end_time=end_time, day=day, table=table)
        slot.save()
        for signup_slot in range(max_number_of_users):
            TimeTableSlotSignup(time_table_slot=slot).save()


class TimeTableSlotSignup(models.Model):
    """
    A single signup for a time table slot for the office hours
    """
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    time_table_slot = models.ForeignKey(TimeTableSlot, on_delete=models.CASCADE)
