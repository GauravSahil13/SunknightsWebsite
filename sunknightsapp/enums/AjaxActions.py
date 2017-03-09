from enum import IntEnum,unique

@unique
class AjaxAction(IntEnum):
    GETTOURNAMENTS=1
    CREATETOURNAMENT=2
    EDITTOURNAMENT=3
    DELETETOURNAMENT=4
    SUBMITPOINTS=5
    RETRIEVEUSERSUBMISSIONS=6
    DECIDEUSERPOINTUSUBMISSION=7
    SUBMITFIGHTS=8
    RETRIEVEFIGHTSSUBMISSIONS=9
    DECIDEFIGHTSSUBMISSION=10
    REVERTSUBMISSION=11
    RETRIEVELEADERBOARD=12
    RETRIEVEUSERSTOFIGHTAGAINST=13
    SUBMITEVENTSQUESTS=14
    DECIDEEVENTQUESTS=15
    RETRIEVEEVENTQUESTSSUBMISSIONS=16
    CHANGEDESC=17
    SUBMITQUESTTASK=18
    RETRIEVEQUESTS=19
    EDITQUESTTASK=20
    DELETEQUESTTASK=21
    ADDQUESTBUILD=22
    EDITQUESTBUILD=23
    DELETEQUESTBUILD=24
    ADDMULTIPLIER=25
    EDITMULTIPLIER=26
    REMOVEMULTIPLIER=27
    SAVEPREFERENCES=28
