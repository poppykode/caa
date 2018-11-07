# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class McAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    alwaysshowdescription = models.IntegerField()
    nosubmissions = models.IntegerField()
    submissiondrafts = models.IntegerField()
    sendnotifications = models.IntegerField()
    sendlatenotifications = models.IntegerField()
    duedate = models.BigIntegerField()
    allowsubmissionsfromdate = models.BigIntegerField()
    grade = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requiresubmissionstatement = models.IntegerField()
    completionsubmit = models.IntegerField()
    cutoffdate = models.BigIntegerField()
    teamsubmission = models.IntegerField()
    requireallteammemberssubmit = models.IntegerField()
    teamsubmissiongroupingid = models.BigIntegerField()
    blindmarking = models.IntegerField()
    revealidentities = models.IntegerField()
    attemptreopenmethod = models.CharField(max_length=10)
    maxattempts = models.IntegerField()
    markingworkflow = models.IntegerField()
    markingallocation = models.IntegerField()
    sendstudentnotifications = models.IntegerField()
    preventsubmissionnotingroup = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assign'


class McAssignGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    grader = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    attemptnumber = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assign_grades'
        unique_together = (('assignment', 'userid', 'attemptnumber'),)


class McAssignPluginConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    plugin = models.CharField(max_length=28)
    subtype = models.CharField(max_length=28)
    name = models.CharField(max_length=28)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_assign_plugin_config'


class McAssignSubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    status = models.CharField(max_length=10, blank=True, null=True)
    groupid = models.BigIntegerField()
    attemptnumber = models.BigIntegerField()
    latest = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assign_submission'
        unique_together = (('assignment', 'userid', 'groupid', 'attemptnumber'),)


class McAssignUserFlags(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    assignment = models.BigIntegerField()
    locked = models.BigIntegerField()
    mailed = models.SmallIntegerField()
    extensionduedate = models.BigIntegerField()
    workflowstate = models.CharField(max_length=20, blank=True, null=True)
    allocatedmarker = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assign_user_flags'


class McAssignUserMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assign_user_mapping'


class McAssignfeedbackComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    grade = models.BigIntegerField()
    commenttext = models.TextField(blank=True, null=True)
    commentformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignfeedback_comments'


class McAssignfeedbackEditpdfAnnot(models.Model):
    id = models.BigAutoField(primary_key=True)
    gradeid = models.BigIntegerField()
    pageno = models.BigIntegerField()
    x = models.BigIntegerField(blank=True, null=True)
    y = models.BigIntegerField(blank=True, null=True)
    endx = models.BigIntegerField(blank=True, null=True)
    endy = models.BigIntegerField(blank=True, null=True)
    path = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    colour = models.CharField(max_length=10, blank=True, null=True)
    draft = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignfeedback_editpdf_annot'


class McAssignfeedbackEditpdfCmnt(models.Model):
    id = models.BigAutoField(primary_key=True)
    gradeid = models.BigIntegerField()
    x = models.BigIntegerField(blank=True, null=True)
    y = models.BigIntegerField(blank=True, null=True)
    width = models.BigIntegerField(blank=True, null=True)
    rawtext = models.TextField(blank=True, null=True)
    pageno = models.BigIntegerField()
    colour = models.CharField(max_length=10, blank=True, null=True)
    draft = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignfeedback_editpdf_cmnt'


class McAssignfeedbackEditpdfQuick(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    rawtext = models.TextField()
    width = models.BigIntegerField()
    colour = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_assignfeedback_editpdf_quick'


class McAssignfeedbackFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    grade = models.BigIntegerField()
    numfiles = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignfeedback_file'


class McAssignment(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    assignmenttype = models.CharField(max_length=50)
    resubmit = models.IntegerField()
    preventlate = models.IntegerField()
    emailteachers = models.IntegerField()
    var1 = models.BigIntegerField(blank=True, null=True)
    var2 = models.BigIntegerField(blank=True, null=True)
    var3 = models.BigIntegerField(blank=True, null=True)
    var4 = models.BigIntegerField(blank=True, null=True)
    var5 = models.BigIntegerField(blank=True, null=True)
    maxbytes = models.BigIntegerField()
    timedue = models.BigIntegerField()
    timeavailable = models.BigIntegerField()
    grade = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignment'


class McAssignmentSubmissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    numfiles = models.BigIntegerField()
    data1 = models.TextField(blank=True, null=True)
    data2 = models.TextField(blank=True, null=True)
    grade = models.BigIntegerField()
    submissioncomment = models.TextField()
    format = models.SmallIntegerField()
    teacher = models.BigIntegerField()
    timemarked = models.BigIntegerField()
    mailed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignment_submissions'


class McAssignmentUpgrade(models.Model):
    id = models.BigAutoField(primary_key=True)
    oldcmid = models.BigIntegerField()
    oldinstance = models.BigIntegerField()
    newcmid = models.BigIntegerField()
    newinstance = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignment_upgrade'


class McAssignsubmissionFile(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    submission = models.BigIntegerField()
    numfiles = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignsubmission_file'


class McAssignsubmissionOnlinetext(models.Model):
    id = models.BigAutoField(primary_key=True)
    assignment = models.BigIntegerField()
    submission = models.BigIntegerField()
    onlinetext = models.TextField(blank=True, null=True)
    onlineformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_assignsubmission_onlinetext'


class McAttendanceregister(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=20)
    offlinesessions = models.IntegerField()
    sessiontimeout = models.SmallIntegerField()
    dayscertificable = models.SmallIntegerField()
    offlinecomments = models.IntegerField()
    mandatoryofflinecomm = models.IntegerField()
    offlinespecifycourse = models.IntegerField()
    mandofflspeccourse = models.IntegerField()
    timemodified = models.BigIntegerField()
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    pendingrecalc = models.IntegerField()
    completiontotaldurationmins = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_attendanceregister'


class McAttendanceregisterAggregate(models.Model):
    id = models.BigAutoField(primary_key=True)
    register = models.BigIntegerField()
    userid = models.BigIntegerField()
    duration = models.BigIntegerField()
    onlinesess = models.IntegerField(blank=True, null=True)
    total = models.IntegerField()
    grandtotal = models.IntegerField()
    refcourse = models.BigIntegerField(blank=True, null=True)
    lastsessionlogout = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_attendanceregister_aggregate'


class McAttendanceregisterLock(models.Model):
    id = models.BigAutoField(primary_key=True)
    register = models.BigIntegerField()
    userid = models.BigIntegerField()
    takenon = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_attendanceregister_lock'


class McAttendanceregisterSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    register = models.BigIntegerField()
    login = models.BigIntegerField()
    logout = models.BigIntegerField()
    duration = models.BigIntegerField()
    userid = models.BigIntegerField()
    onlinesess = models.IntegerField()
    refcourse = models.BigIntegerField(blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    addedbyuserid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_attendanceregister_session'


class McBackupControllers(models.Model):
    id = models.BigAutoField(primary_key=True)
    backupid = models.CharField(unique=True, max_length=32)
    operation = models.CharField(max_length=20)
    type = models.CharField(max_length=10)
    itemid = models.BigIntegerField()
    format = models.CharField(max_length=20)
    interactive = models.SmallIntegerField()
    purpose = models.SmallIntegerField()
    userid = models.BigIntegerField()
    status = models.SmallIntegerField()
    execution = models.SmallIntegerField()
    executiontime = models.BigIntegerField()
    checksum = models.CharField(max_length=32)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    controller = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_backup_controllers'


class McBackupCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(unique=True)
    laststarttime = models.BigIntegerField()
    lastendtime = models.BigIntegerField()
    laststatus = models.CharField(max_length=1)
    nextstarttime = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_backup_courses'


class McBackupLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    backupid = models.CharField(max_length=32)
    loglevel = models.SmallIntegerField()
    message = models.TextField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_backup_logs'
        unique_together = (('backupid', 'id'),)


class McBadge(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usercreated = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    issuername = models.CharField(max_length=255)
    issuerurl = models.CharField(max_length=255)
    issuercontact = models.CharField(max_length=255, blank=True, null=True)
    expiredate = models.BigIntegerField(blank=True, null=True)
    expireperiod = models.BigIntegerField(blank=True, null=True)
    type = models.IntegerField()
    courseid = models.BigIntegerField(blank=True, null=True)
    message = models.TextField()
    messagesubject = models.TextField()
    attachment = models.IntegerField()
    notification = models.IntegerField()
    status = models.IntegerField()
    nextcron = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_badge'


class McBadgeBackpack(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    email = models.CharField(max_length=100)
    backpackurl = models.CharField(max_length=255)
    backpackuid = models.BigIntegerField()
    autosync = models.IntegerField()
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_badge_backpack'


class McBadgeCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    badgeid = models.BigIntegerField()
    criteriatype = models.BigIntegerField(blank=True, null=True)
    method = models.IntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_badge_criteria'
        unique_together = (('badgeid', 'criteriatype'),)


class McBadgeCriteriaMet(models.Model):
    id = models.BigAutoField(primary_key=True)
    issuedid = models.BigIntegerField(blank=True, null=True)
    critid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datemet = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_badge_criteria_met'


class McBadgeCriteriaParam(models.Model):
    id = models.BigAutoField(primary_key=True)
    critid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_badge_criteria_param'


class McBadgeExternal(models.Model):
    id = models.BigAutoField(primary_key=True)
    backpackid = models.BigIntegerField()
    collectionid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_badge_external'


class McBadgeIssued(models.Model):
    id = models.BigAutoField(primary_key=True)
    badgeid = models.BigIntegerField()
    userid = models.BigIntegerField()
    uniquehash = models.TextField()
    dateissued = models.BigIntegerField()
    dateexpire = models.BigIntegerField(blank=True, null=True)
    visible = models.IntegerField()
    issuernotified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_badge_issued'
        unique_together = (('badgeid', 'userid'),)


class McBadgeManualAward(models.Model):
    id = models.BigAutoField(primary_key=True)
    badgeid = models.BigIntegerField()
    recipientid = models.BigIntegerField()
    issuerid = models.BigIntegerField()
    issuerrole = models.BigIntegerField()
    datemet = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_badge_manual_award'


class McBigbluebuttonbn(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    meetingid = models.CharField(max_length=256, blank=True, null=True)
    moderatorpass = models.CharField(max_length=255)
    viewerpass = models.CharField(max_length=255)
    wait = models.IntegerField()
    record = models.IntegerField()
    tagging = models.IntegerField()
    welcome = models.TextField(blank=True, null=True)
    voicebridge = models.IntegerField()
    openingtime = models.BigIntegerField()
    closingtime = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    presentation = models.TextField(blank=True, null=True)
    participants = models.TextField(blank=True, null=True)
    userlimit = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_bigbluebuttonbn'


class McBigbluebuttonbnLogs(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    bigbluebuttonbnid = models.BigIntegerField()
    userid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    meetingid = models.CharField(max_length=256)
    log = models.CharField(max_length=32)
    meta = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_bigbluebuttonbn_logs'


class McBlock(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=40)
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_block'


class McBlockCommunity(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    coursename = models.CharField(max_length=255)
    coursedescription = models.TextField(blank=True, null=True)
    courseurl = models.CharField(max_length=255)
    imageurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_block_community'


class McBlockInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    blockname = models.CharField(max_length=40)
    parentcontextid = models.BigIntegerField()
    showinsubcontexts = models.SmallIntegerField()
    pagetypepattern = models.CharField(max_length=64)
    subpagepattern = models.CharField(max_length=16, blank=True, null=True)
    defaultregion = models.CharField(max_length=16)
    defaultweight = models.BigIntegerField()
    configdata = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_block_instances'


class McBlockNotificationsCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField(blank=True, null=True)
    last_notification_time = models.BigIntegerField(blank=True, null=True)
    notify_by_email = models.IntegerField(blank=True, null=True)
    notify_by_sms = models.IntegerField(blank=True, null=True)
    notify_by_rss = models.IntegerField(blank=True, null=True)
    email_notification_preset = models.IntegerField(blank=True, null=True)
    sms_notification_preset = models.IntegerField(blank=True, null=True)
    rss_shortname_url_param = models.IntegerField(blank=True, null=True)
    history_length = models.BigIntegerField()
    calendar_event_created = models.IntegerField(blank=True, null=True)
    calendar_event_deleted = models.IntegerField(blank=True, null=True)
    calendar_event_updated = models.IntegerField(blank=True, null=True)
    course_module_created = models.IntegerField(blank=True, null=True)
    course_module_deleted = models.IntegerField(blank=True, null=True)
    course_module_updated = models.IntegerField(blank=True, null=True)
    chapter_created = models.IntegerField(blank=True, null=True)
    chapter_deleted = models.IntegerField(blank=True, null=True)
    chapter_updated = models.IntegerField(blank=True, null=True)
    field_created = models.IntegerField(blank=True, null=True)
    field_deleted = models.IntegerField(blank=True, null=True)
    field_updated = models.IntegerField(blank=True, null=True)
    record_created = models.IntegerField(blank=True, null=True)
    record_deleted = models.IntegerField(blank=True, null=True)
    record_updated = models.IntegerField(blank=True, null=True)
    template_updated = models.IntegerField(blank=True, null=True)
    folder_updated = models.IntegerField(blank=True, null=True)
    discussion_created = models.IntegerField(blank=True, null=True)
    discussion_deleted = models.IntegerField(blank=True, null=True)
    discussion_moved = models.IntegerField(blank=True, null=True)
    discussion_updated = models.IntegerField(blank=True, null=True)
    post_created = models.IntegerField(blank=True, null=True)
    post_deleted = models.IntegerField(blank=True, null=True)
    post_updated = models.IntegerField(blank=True, null=True)
    category_created = models.IntegerField(blank=True, null=True)
    category_deleted = models.IntegerField(blank=True, null=True)
    category_updated = models.IntegerField(blank=True, null=True)
    glossary_comment_created = models.IntegerField(blank=True, null=True)
    glossary_comment_deleted = models.IntegerField(blank=True, null=True)
    entry_approved = models.IntegerField(blank=True, null=True)
    entry_created = models.IntegerField(blank=True, null=True)
    entry_deleted = models.IntegerField(blank=True, null=True)
    entry_disapproved = models.IntegerField(blank=True, null=True)
    entry_updated = models.IntegerField(blank=True, null=True)
    wiki_comment_created = models.IntegerField(blank=True, null=True)
    wiki_comment_deleted = models.IntegerField(blank=True, null=True)
    page_created = models.IntegerField(blank=True, null=True)
    page_deleted = models.IntegerField(blank=True, null=True)
    page_updated = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_block_notifications_courses'


class McBlockNotificationsLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField()
    event = models.CharField(max_length=255)
    module = models.CharField(max_length=255)
    module_id = models.BigIntegerField()
    name = models.CharField(max_length=255)
    target = models.CharField(max_length=100, blank=True, null=True)
    target_id = models.BigIntegerField(blank=True, null=True)
    time_created = models.BigIntegerField()
    other = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_block_notifications_log'


class McBlockNotificationsUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.BigIntegerField(blank=True, null=True)
    course_id = models.BigIntegerField(blank=True, null=True)
    notify_by_email = models.IntegerField(blank=True, null=True)
    notify_by_sms = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_block_notifications_users'


class McBlockPositions(models.Model):
    id = models.BigAutoField(primary_key=True)
    blockinstanceid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    pagetype = models.CharField(max_length=64)
    subpage = models.CharField(max_length=16)
    visible = models.SmallIntegerField()
    region = models.CharField(max_length=16)
    weight = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_block_positions'
        unique_together = (('blockinstanceid', 'contextid', 'pagetype', 'subpage'),)


class McBlockRecentActivity(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    cmid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField()
    action = models.IntegerField()
    modname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_block_recent_activity'


class McBlockRssClient(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    title = models.TextField()
    preferredtitle = models.CharField(max_length=64)
    description = models.TextField()
    shared = models.IntegerField()
    url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_block_rss_client'


class McBlogAssociation(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    blogid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_blog_association'


class McBlogExternal(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    url = models.TextField()
    filtertags = models.CharField(max_length=255, blank=True, null=True)
    failedlastsync = models.IntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    timefetched = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_blog_external'


class McBook(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    numbering = models.SmallIntegerField()
    navstyle = models.SmallIntegerField()
    customtitles = models.IntegerField()
    revision = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_book'


class McBookChapters(models.Model):
    id = models.BigAutoField(primary_key=True)
    bookid = models.BigIntegerField()
    pagenum = models.BigIntegerField()
    subchapter = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField()
    contentformat = models.SmallIntegerField()
    hidden = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    importsrc = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_book_chapters'


class McCacheFilters(models.Model):
    id = models.BigAutoField(primary_key=True)
    filter = models.CharField(max_length=32)
    version = models.BigIntegerField()
    md5key = models.CharField(max_length=32)
    rawtext = models.TextField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_cache_filters'


class McCacheFlags(models.Model):
    id = models.BigAutoField(primary_key=True)
    flagtype = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    value = models.TextField()
    expiry = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_cache_flags'


class McCapabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    captype = models.CharField(max_length=50)
    contextlevel = models.BigIntegerField()
    component = models.CharField(max_length=100)
    riskbitmask = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_capabilities'


class McChat(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    keepdays = models.BigIntegerField()
    studentlogs = models.SmallIntegerField()
    chattime = models.BigIntegerField()
    schedule = models.SmallIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_chat'


class McChatMessages(models.Model):
    id = models.BigAutoField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    system = models.IntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_chat_messages'


class McChatMessagesCurrent(models.Model):
    id = models.BigAutoField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    system = models.IntegerField()
    message = models.TextField()
    timestamp = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_chat_messages_current'


class McChatUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    chatid = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    version = models.CharField(max_length=16)
    ip = models.CharField(max_length=45)
    firstping = models.BigIntegerField()
    lastping = models.BigIntegerField()
    lastmessageping = models.BigIntegerField()
    sid = models.CharField(max_length=32)
    course = models.BigIntegerField()
    lang = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mc_chat_users'


class McChoice(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    publish = models.IntegerField()
    showresults = models.IntegerField()
    display = models.SmallIntegerField()
    allowupdate = models.IntegerField()
    allowmultiple = models.IntegerField()
    showunanswered = models.IntegerField()
    includeinactive = models.IntegerField()
    limitanswers = models.IntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    showpreview = models.IntegerField()
    timemodified = models.BigIntegerField()
    completionsubmit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_choice'


class McChoiceAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    choiceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    optionid = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_choice_answers'


class McChoiceOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    choiceid = models.BigIntegerField()
    text = models.TextField(blank=True, null=True)
    maxanswers = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_choice_options'


class McCohort(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=254)
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    visible = models.IntegerField()
    component = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_cohort'


class McCohortMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    cohortid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timeadded = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_cohort_members'
        unique_together = (('cohortid', 'userid'),)


class McComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=255, blank=True, null=True)
    commentarea = models.CharField(max_length=255)
    itemid = models.BigIntegerField()
    content = models.TextField()
    format = models.IntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_comments'


class McConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_config'


class McConfigLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    plugin = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)
    oldvalue = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_config_log'


class McConfigPlugins(models.Model):
    id = models.BigAutoField(primary_key=True)
    plugin = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_config_plugins'
        unique_together = (('plugin', 'name'),)


class McContext(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextlevel = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    depth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_context'
        unique_together = (('contextlevel', 'instanceid'),)


class McContextTemp(models.Model):
    id = models.BigIntegerField(primary_key=True)
    path = models.CharField(max_length=255)
    depth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_context_temp'


class McCourse(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    format = models.CharField(max_length=21)
    showgrades = models.IntegerField()
    newsitems = models.IntegerField()
    startdate = models.BigIntegerField()
    marker = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    legacyfiles = models.SmallIntegerField()
    showreports = models.SmallIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.SmallIntegerField()
    groupmodeforce = models.SmallIntegerField()
    defaultgroupingid = models.BigIntegerField()
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    requested = models.IntegerField()
    enablecompletion = models.IntegerField()
    completionnotify = models.IntegerField()
    cacherev = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_course'


class McCourseCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    coursecount = models.BigIntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    timemodified = models.BigIntegerField()
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255)
    theme = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_categories'


class McCourseCompletionAggrMethd(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    criteriatype = models.BigIntegerField(blank=True, null=True)
    method = models.IntegerField()
    value = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_completion_aggr_methd'
        unique_together = (('course', 'criteriatype'),)


class McCourseCompletionCritCompl(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    criteriaid = models.BigIntegerField()
    gradefinal = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    unenroled = models.BigIntegerField(blank=True, null=True)
    timecompleted = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_completion_crit_compl'
        unique_together = (('userid', 'course', 'criteriaid'),)


class McCourseCompletionCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    criteriatype = models.BigIntegerField()
    module = models.CharField(max_length=100, blank=True, null=True)
    moduleinstance = models.BigIntegerField(blank=True, null=True)
    courseinstance = models.BigIntegerField(blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    timeend = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    role = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_completion_criteria'


class McCourseCompletions(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    course = models.BigIntegerField()
    timeenrolled = models.BigIntegerField()
    timestarted = models.BigIntegerField()
    timecompleted = models.BigIntegerField(blank=True, null=True)
    reaggregate = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_course_completions'
        unique_together = (('userid', 'course'),)


class McCourseFormatOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    format = models.CharField(max_length=21)
    sectionid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_format_options'
        unique_together = (('courseid', 'format', 'sectionid', 'name'),)


class McCourseModules(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    module = models.BigIntegerField()
    instance = models.BigIntegerField()
    section = models.BigIntegerField()
    idnumber = models.CharField(max_length=100, blank=True, null=True)
    added = models.BigIntegerField()
    score = models.SmallIntegerField()
    indent = models.IntegerField()
    visible = models.IntegerField()
    visibleold = models.IntegerField()
    groupmode = models.SmallIntegerField()
    groupingid = models.BigIntegerField()
    completion = models.IntegerField()
    completiongradeitemnumber = models.BigIntegerField(blank=True, null=True)
    completionview = models.IntegerField()
    completionexpected = models.BigIntegerField()
    showdescription = models.IntegerField()
    availability = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_modules'


class McCourseModulesCompletion(models.Model):
    id = models.BigAutoField(primary_key=True)
    coursemoduleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    completionstate = models.IntegerField()
    viewed = models.IntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_course_modules_completion'
        unique_together = (('userid', 'coursemoduleid'),)


class McCoursePublished(models.Model):
    id = models.BigAutoField(primary_key=True)
    huburl = models.CharField(max_length=255, blank=True, null=True)
    courseid = models.BigIntegerField()
    timepublished = models.BigIntegerField()
    enrollable = models.IntegerField()
    hubcourseid = models.BigIntegerField()
    status = models.IntegerField(blank=True, null=True)
    timechecked = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_published'


class McCourseRequest(models.Model):
    id = models.BigAutoField(primary_key=True)
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    summary = models.TextField()
    summaryformat = models.IntegerField()
    category = models.BigIntegerField()
    reason = models.TextField()
    requester = models.BigIntegerField()
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mc_course_request'


class McCourseSections(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    section = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    summaryformat = models.IntegerField()
    sequence = models.TextField(blank=True, null=True)
    visible = models.IntegerField()
    availability = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_course_sections'
        unique_together = (('course', 'section'),)


class McData(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    comments = models.SmallIntegerField()
    timeavailablefrom = models.BigIntegerField()
    timeavailableto = models.BigIntegerField()
    timeviewfrom = models.BigIntegerField()
    timeviewto = models.BigIntegerField()
    requiredentries = models.IntegerField()
    requiredentriestoview = models.IntegerField()
    maxentries = models.IntegerField()
    rssarticles = models.SmallIntegerField()
    singletemplate = models.TextField(blank=True, null=True)
    listtemplate = models.TextField(blank=True, null=True)
    listtemplateheader = models.TextField(blank=True, null=True)
    listtemplatefooter = models.TextField(blank=True, null=True)
    addtemplate = models.TextField(blank=True, null=True)
    rsstemplate = models.TextField(blank=True, null=True)
    rsstitletemplate = models.TextField(blank=True, null=True)
    csstemplate = models.TextField(blank=True, null=True)
    jstemplate = models.TextField(blank=True, null=True)
    asearchtemplate = models.TextField(blank=True, null=True)
    approval = models.SmallIntegerField()
    scale = models.BigIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    defaultsort = models.BigIntegerField()
    defaultsortdir = models.SmallIntegerField()
    editany = models.SmallIntegerField()
    notification = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_data'


class McDataContent(models.Model):
    id = models.BigAutoField(primary_key=True)
    fieldid = models.BigIntegerField()
    recordid = models.BigIntegerField()
    content = models.TextField(blank=True, null=True)
    content1 = models.TextField(blank=True, null=True)
    content2 = models.TextField(blank=True, null=True)
    content3 = models.TextField(blank=True, null=True)
    content4 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_data_content'


class McDataFields(models.Model):
    id = models.BigAutoField(primary_key=True)
    dataid = models.BigIntegerField()
    type = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    required = models.IntegerField()
    param1 = models.TextField(blank=True, null=True)
    param2 = models.TextField(blank=True, null=True)
    param3 = models.TextField(blank=True, null=True)
    param4 = models.TextField(blank=True, null=True)
    param5 = models.TextField(blank=True, null=True)
    param6 = models.TextField(blank=True, null=True)
    param7 = models.TextField(blank=True, null=True)
    param8 = models.TextField(blank=True, null=True)
    param9 = models.TextField(blank=True, null=True)
    param10 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_data_fields'


class McDataRecords(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    dataid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    approved = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_data_records'


class McEditorAttoAutosave(models.Model):
    id = models.BigAutoField(primary_key=True)
    elementid = models.CharField(max_length=255)
    contextid = models.BigIntegerField()
    pagehash = models.CharField(max_length=64)
    userid = models.BigIntegerField()
    drafttext = models.TextField()
    draftid = models.BigIntegerField(blank=True, null=True)
    pageinstance = models.CharField(max_length=64)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_editor_atto_autosave'
        unique_together = (('elementid', 'contextid', 'userid', 'pagehash'),)


class McEnrol(models.Model):
    id = models.BigAutoField(primary_key=True)
    enrol = models.CharField(max_length=20)
    status = models.BigIntegerField()
    courseid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    name = models.CharField(max_length=255, blank=True, null=True)
    enrolperiod = models.BigIntegerField(blank=True, null=True)
    enrolstartdate = models.BigIntegerField(blank=True, null=True)
    enrolenddate = models.BigIntegerField(blank=True, null=True)
    expirynotify = models.IntegerField(blank=True, null=True)
    expirythreshold = models.BigIntegerField(blank=True, null=True)
    notifyall = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)
    cost = models.CharField(max_length=20, blank=True, null=True)
    currency = models.CharField(max_length=3, blank=True, null=True)
    roleid = models.BigIntegerField(blank=True, null=True)
    customint1 = models.BigIntegerField(blank=True, null=True)
    customint2 = models.BigIntegerField(blank=True, null=True)
    customint3 = models.BigIntegerField(blank=True, null=True)
    customint4 = models.BigIntegerField(blank=True, null=True)
    customint5 = models.BigIntegerField(blank=True, null=True)
    customint6 = models.BigIntegerField(blank=True, null=True)
    customint7 = models.BigIntegerField(blank=True, null=True)
    customint8 = models.BigIntegerField(blank=True, null=True)
    customchar1 = models.CharField(max_length=255, blank=True, null=True)
    customchar2 = models.CharField(max_length=255, blank=True, null=True)
    customchar3 = models.CharField(max_length=1333, blank=True, null=True)
    customdec1 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customdec2 = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    customtext1 = models.TextField(blank=True, null=True)
    customtext2 = models.TextField(blank=True, null=True)
    customtext3 = models.TextField(blank=True, null=True)
    customtext4 = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_enrol'


class McEnrolFlatfile(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.CharField(max_length=30)
    roleid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_enrol_flatfile'


class McEnrolPaypal(models.Model):
    id = models.BigAutoField(primary_key=True)
    business = models.CharField(max_length=255)
    receiver_email = models.CharField(max_length=255)
    receiver_id = models.CharField(max_length=255)
    item_name = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    instanceid = models.BigIntegerField()
    memo = models.CharField(max_length=255)
    tax = models.CharField(max_length=255)
    option_name1 = models.CharField(max_length=255)
    option_selection1_x = models.CharField(max_length=255)
    option_name2 = models.CharField(max_length=255)
    option_selection2_x = models.CharField(max_length=255)
    payment_status = models.CharField(max_length=255)
    pending_reason = models.CharField(max_length=255)
    reason_code = models.CharField(max_length=30)
    txn_id = models.CharField(max_length=255)
    parent_txn_id = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=30)
    timeupdated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_enrol_paypal'


class McEvent(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.TextField()
    description = models.TextField()
    format = models.SmallIntegerField()
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    repeatid = models.BigIntegerField()
    modulename = models.CharField(max_length=20)
    instance = models.BigIntegerField()
    eventtype = models.CharField(max_length=20)
    timestart = models.BigIntegerField()
    timeduration = models.BigIntegerField()
    visible = models.SmallIntegerField()
    uuid = models.CharField(max_length=255)
    sequence = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    subscriptionid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_event'


class McEventSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    url = models.CharField(max_length=255)
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    eventtype = models.CharField(max_length=20)
    pollinterval = models.BigIntegerField()
    lastupdated = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_event_subscriptions'


class McEventsHandlers(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=166)
    component = models.CharField(max_length=166)
    handlerfile = models.CharField(max_length=255)
    handlerfunction = models.TextField(blank=True, null=True)
    schedule = models.CharField(max_length=255, blank=True, null=True)
    status = models.BigIntegerField()
    internal = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_events_handlers'
        unique_together = (('eventname', 'component'),)


class McEventsQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventdata = models.TextField()
    stackdump = models.TextField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_events_queue'


class McEventsQueueHandlers(models.Model):
    id = models.BigAutoField(primary_key=True)
    queuedeventid = models.BigIntegerField()
    handlerid = models.BigIntegerField()
    status = models.BigIntegerField(blank=True, null=True)
    errormessage = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_events_queue_handlers'


class McExternalFunctions(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    classname = models.CharField(max_length=100)
    methodname = models.CharField(max_length=100)
    classpath = models.CharField(max_length=255, blank=True, null=True)
    component = models.CharField(max_length=100)
    capabilities = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_external_functions'


class McExternalServices(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=200)
    enabled = models.IntegerField()
    requiredcapability = models.CharField(max_length=150, blank=True, null=True)
    restrictedusers = models.IntegerField()
    component = models.CharField(max_length=100, blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    downloadfiles = models.IntegerField()
    uploadfiles = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_external_services'


class McExternalServicesFunctions(models.Model):
    id = models.BigAutoField(primary_key=True)
    externalserviceid = models.BigIntegerField()
    functionname = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'mc_external_services_functions'


class McExternalServicesUsers(models.Model):
    id = models.BigAutoField(primary_key=True)
    externalserviceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    iprestriction = models.CharField(max_length=255, blank=True, null=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_external_services_users'


class McExternalTokens(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=128)
    tokentype = models.SmallIntegerField()
    userid = models.BigIntegerField()
    externalserviceid = models.BigIntegerField()
    sid = models.CharField(max_length=128, blank=True, null=True)
    contextid = models.BigIntegerField()
    creatorid = models.BigIntegerField()
    iprestriction = models.CharField(max_length=255, blank=True, null=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    lastaccess = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_external_tokens'


class McFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    anonymous = models.IntegerField()
    email_notification = models.IntegerField()
    multiple_submit = models.IntegerField()
    autonumbering = models.IntegerField()
    site_after_submit = models.CharField(max_length=255)
    page_after_submit = models.TextField()
    page_after_submitformat = models.IntegerField()
    publish_stats = models.IntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionsubmit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_feedback'


class McFeedbackCompleted(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    random_response = models.BigIntegerField()
    anonymous_response = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_feedback_completed'


class McFeedbackCompletedtmp(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.BigIntegerField()
    userid = models.BigIntegerField()
    guestid = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    random_response = models.BigIntegerField()
    anonymous_response = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_feedback_completedtmp'


class McFeedbackItem(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedback = models.BigIntegerField()
    template = models.BigIntegerField()
    name = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    presentation = models.TextField()
    typ = models.CharField(max_length=255)
    hasvalue = models.IntegerField()
    position = models.SmallIntegerField()
    required = models.IntegerField()
    dependitem = models.BigIntegerField()
    dependvalue = models.CharField(max_length=255)
    options = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_feedback_item'


class McFeedbackSitecourseMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    feedbackid = models.BigIntegerField()
    courseid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_feedback_sitecourse_map'


class McFeedbackTemplate(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    ispublic = models.IntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_feedback_template'


class McFeedbackTracking(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    feedback = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_feedback_tracking'


class McFeedbackValue(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField()
    item = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_feedback_value'


class McFeedbackValuetmp(models.Model):
    id = models.BigAutoField(primary_key=True)
    course_id = models.BigIntegerField()
    item = models.BigIntegerField()
    completed = models.BigIntegerField()
    tmp_completed = models.BigIntegerField()
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_feedback_valuetmp'


class McFiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    contenthash = models.CharField(max_length=40)
    pathnamehash = models.CharField(unique=True, max_length=40)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    filearea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    filepath = models.CharField(max_length=255)
    filename = models.CharField(max_length=255)
    userid = models.BigIntegerField(blank=True, null=True)
    filesize = models.BigIntegerField()
    mimetype = models.CharField(max_length=100, blank=True, null=True)
    status = models.BigIntegerField()
    source = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    license = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    referencefileid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_files'


class McFilesReference(models.Model):
    id = models.BigAutoField(primary_key=True)
    repositoryid = models.BigIntegerField()
    lastsync = models.BigIntegerField(blank=True, null=True)
    reference = models.TextField(blank=True, null=True)
    referencehash = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'mc_files_reference'
        unique_together = (('referencehash', 'repositoryid'),)


class McFilterActive(models.Model):
    id = models.BigAutoField(primary_key=True)
    filter = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    active = models.SmallIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_filter_active'
        unique_together = (('contextid', 'filter'),)


class McFilterConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    filter = models.CharField(max_length=32)
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_filter_config'
        unique_together = (('contextid', 'filter', 'name'),)


class McFolder(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    display = models.SmallIntegerField()
    showexpanded = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_folder'


class McForum(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    type = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    maxbytes = models.BigIntegerField()
    maxattachments = models.BigIntegerField()
    forcesubscribe = models.IntegerField()
    trackingtype = models.IntegerField()
    rsstype = models.IntegerField()
    rssarticles = models.IntegerField()
    timemodified = models.BigIntegerField()
    warnafter = models.BigIntegerField()
    blockafter = models.BigIntegerField()
    blockperiod = models.BigIntegerField()
    completiondiscussions = models.IntegerField()
    completionreplies = models.IntegerField()
    completionposts = models.IntegerField()
    displaywordcount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum'


class McForumDigests(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forum = models.BigIntegerField()
    maildigest = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_digests'
        unique_together = (('forum', 'userid', 'maildigest'),)


class McForumDiscussionSubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    forum = models.BigIntegerField()
    userid = models.BigIntegerField()
    discussion = models.BigIntegerField()
    preference = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_discussion_subs'
        unique_together = (('userid', 'discussion'),)


class McForumDiscussions(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    forum = models.BigIntegerField()
    name = models.CharField(max_length=255)
    firstpost = models.BigIntegerField()
    userid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    assessed = models.IntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_discussions'


class McForumPosts(models.Model):
    id = models.BigAutoField(primary_key=True)
    discussion = models.BigIntegerField()
    parent = models.BigIntegerField()
    userid = models.BigIntegerField()
    created = models.BigIntegerField()
    modified = models.BigIntegerField()
    mailed = models.IntegerField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    messageformat = models.IntegerField()
    messagetrust = models.IntegerField()
    attachment = models.CharField(max_length=100)
    totalscore = models.SmallIntegerField()
    mailnow = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_posts'


class McForumQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_queue'


class McForumRead(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()
    discussionid = models.BigIntegerField()
    postid = models.BigIntegerField()
    firstread = models.BigIntegerField()
    lastread = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_read'


class McForumSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forum = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_subscriptions'


class McForumTrackPrefs(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    forumid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_forum_track_prefs'


class McGlossary(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    allowduplicatedentries = models.IntegerField()
    displayformat = models.CharField(max_length=50)
    mainglossary = models.IntegerField()
    showspecial = models.IntegerField()
    showalphabet = models.IntegerField()
    showall = models.IntegerField()
    allowcomments = models.IntegerField()
    allowprintview = models.IntegerField()
    usedynalink = models.IntegerField()
    defaultapproval = models.IntegerField()
    approvaldisplayformat = models.CharField(max_length=50)
    globalglossary = models.IntegerField()
    entbypage = models.SmallIntegerField()
    editalways = models.IntegerField()
    rsstype = models.IntegerField()
    rssarticles = models.IntegerField()
    assessed = models.BigIntegerField()
    assesstimestart = models.BigIntegerField()
    assesstimefinish = models.BigIntegerField()
    scale = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionentries = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_glossary'


class McGlossaryAlias(models.Model):
    id = models.BigAutoField(primary_key=True)
    entryid = models.BigIntegerField()
    alias = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_glossary_alias'


class McGlossaryCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    glossaryid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    usedynalink = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_glossary_categories'


class McGlossaryEntries(models.Model):
    id = models.BigAutoField(primary_key=True)
    glossaryid = models.BigIntegerField()
    userid = models.BigIntegerField()
    concept = models.CharField(max_length=255)
    definition = models.TextField()
    definitionformat = models.IntegerField()
    definitiontrust = models.IntegerField()
    attachment = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    teacherentry = models.IntegerField()
    sourceglossaryid = models.BigIntegerField()
    usedynalink = models.IntegerField()
    casesensitive = models.IntegerField()
    fullmatch = models.IntegerField()
    approved = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_glossary_entries'


class McGlossaryEntriesCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    categoryid = models.BigIntegerField()
    entryid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_glossary_entries_categories'


class McGlossaryFormats(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    popupformatname = models.CharField(max_length=50)
    visible = models.IntegerField()
    showgroup = models.IntegerField()
    defaultmode = models.CharField(max_length=50)
    defaulthook = models.CharField(max_length=50)
    sortkey = models.CharField(max_length=50)
    sortorder = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mc_glossary_formats'


class McGradeCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    parent = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255)
    aggregation = models.BigIntegerField()
    keephigh = models.BigIntegerField()
    droplow = models.BigIntegerField()
    aggregateonlygraded = models.IntegerField()
    aggregateoutcomes = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_categories'


class McGradeCategoriesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField()
    parent = models.BigIntegerField(blank=True, null=True)
    depth = models.BigIntegerField()
    path = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.CharField(max_length=255)
    aggregation = models.BigIntegerField()
    keephigh = models.BigIntegerField()
    droplow = models.BigIntegerField()
    aggregateonlygraded = models.IntegerField()
    aggregateoutcomes = models.IntegerField()
    aggregatesubcats = models.IntegerField()
    hidden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_categories_history'


class McGradeGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.BigIntegerField()
    userid = models.BigIntegerField()
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    exported = models.BigIntegerField()
    overridden = models.BigIntegerField()
    excluded = models.BigIntegerField()
    feedback = models.TextField(blank=True, null=True)
    feedbackformat = models.BigIntegerField()
    information = models.TextField(blank=True, null=True)
    informationformat = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    aggregationstatus = models.CharField(max_length=10)
    aggregationweight = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grade_grades'
        unique_together = (('userid', 'itemid'),)


class McGradeGradesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    itemid = models.BigIntegerField()
    userid = models.BigIntegerField()
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    rawgrademax = models.DecimalField(max_digits=10, decimal_places=5)
    rawgrademin = models.DecimalField(max_digits=10, decimal_places=5)
    rawscaleid = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    exported = models.BigIntegerField()
    overridden = models.BigIntegerField()
    excluded = models.BigIntegerField()
    feedback = models.TextField(blank=True, null=True)
    feedbackformat = models.BigIntegerField()
    information = models.TextField(blank=True, null=True)
    informationformat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_grades_history'


class McGradeImportNewitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemname = models.CharField(max_length=255)
    importcode = models.BigIntegerField()
    importer = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_import_newitem'


class McGradeImportValues(models.Model):
    id = models.BigAutoField(primary_key=True)
    itemid = models.BigIntegerField(blank=True, null=True)
    newgradeitem = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField()
    finalgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)
    importcode = models.BigIntegerField()
    importer = models.BigIntegerField(blank=True, null=True)
    importonlyfeedback = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grade_import_values'


class McGradeItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    categoryid = models.BigIntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30, blank=True, null=True)
    iteminstance = models.BigIntegerField(blank=True, null=True)
    itemnumber = models.BigIntegerField(blank=True, null=True)
    iteminfo = models.TextField(blank=True, null=True)
    idnumber = models.CharField(max_length=255, blank=True, null=True)
    calculation = models.TextField(blank=True, null=True)
    gradetype = models.SmallIntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.BigIntegerField(blank=True, null=True)
    outcomeid = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef2 = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.BigIntegerField()
    display = models.BigIntegerField()
    decimals = models.IntegerField(blank=True, null=True)
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    needsupdate = models.BigIntegerField()
    weightoverride = models.IntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grade_items'


class McGradeItemsHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    categoryid = models.BigIntegerField(blank=True, null=True)
    itemname = models.CharField(max_length=255, blank=True, null=True)
    itemtype = models.CharField(max_length=30)
    itemmodule = models.CharField(max_length=30, blank=True, null=True)
    iteminstance = models.BigIntegerField(blank=True, null=True)
    itemnumber = models.BigIntegerField(blank=True, null=True)
    iteminfo = models.TextField(blank=True, null=True)
    idnumber = models.CharField(max_length=255, blank=True, null=True)
    calculation = models.TextField(blank=True, null=True)
    gradetype = models.SmallIntegerField()
    grademax = models.DecimalField(max_digits=10, decimal_places=5)
    grademin = models.DecimalField(max_digits=10, decimal_places=5)
    scaleid = models.BigIntegerField(blank=True, null=True)
    outcomeid = models.BigIntegerField(blank=True, null=True)
    gradepass = models.DecimalField(max_digits=10, decimal_places=5)
    multfactor = models.DecimalField(max_digits=10, decimal_places=5)
    plusfactor = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef = models.DecimalField(max_digits=10, decimal_places=5)
    aggregationcoef2 = models.DecimalField(max_digits=10, decimal_places=5)
    sortorder = models.BigIntegerField()
    hidden = models.BigIntegerField()
    locked = models.BigIntegerField()
    locktime = models.BigIntegerField()
    needsupdate = models.BigIntegerField()
    display = models.BigIntegerField()
    decimals = models.IntegerField(blank=True, null=True)
    weightoverride = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_items_history'


class McGradeLetters(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    lowerboundary = models.DecimalField(max_digits=10, decimal_places=5)
    letter = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_grade_letters'
        unique_together = (('contextid', 'lowerboundary', 'letter'),)


class McGradeOutcomes(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grade_outcomes'
        unique_together = (('courseid', 'shortname'),)


class McGradeOutcomesCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    outcomeid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_outcomes_courses'
        unique_together = (('courseid', 'outcomeid'),)


class McGradeOutcomesHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField(blank=True, null=True)
    shortname = models.CharField(max_length=255)
    fullname = models.TextField()
    scaleid = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grade_outcomes_history'


class McGradeSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grade_settings'
        unique_together = (('courseid', 'name'),)


class McGradingAreas(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    areaname = models.CharField(max_length=100)
    activemethod = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grading_areas'
        unique_together = (('contextid', 'component', 'areaname'),)


class McGradingDefinitions(models.Model):
    id = models.BigAutoField(primary_key=True)
    areaid = models.BigIntegerField()
    method = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    status = models.BigIntegerField()
    copiedfromid = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    usercreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    usermodified = models.BigIntegerField()
    timecopied = models.BigIntegerField(blank=True, null=True)
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_grading_definitions'
        unique_together = (('areaid', 'method'),)


class McGradingInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    raterid = models.BigIntegerField()
    itemid = models.BigIntegerField(blank=True, null=True)
    rawgrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    status = models.BigIntegerField()
    feedback = models.TextField(blank=True, null=True)
    feedbackformat = models.IntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_grading_instances'


class McGradingformGuideComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_gradingform_guide_comments'


class McGradingformGuideCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    shortname = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField(blank=True, null=True)
    descriptionmarkers = models.TextField(blank=True, null=True)
    descriptionmarkersformat = models.IntegerField(blank=True, null=True)
    maxscore = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mc_gradingform_guide_criteria'


class McGradingformGuideFillings(models.Model):
    id = models.BigAutoField(primary_key=True)
    instanceid = models.BigIntegerField()
    criterionid = models.BigIntegerField()
    remark = models.TextField(blank=True, null=True)
    remarkformat = models.IntegerField(blank=True, null=True)
    score = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mc_gradingform_guide_fillings'
        unique_together = (('instanceid', 'criterionid'),)


class McGradingformRubricCriteria(models.Model):
    id = models.BigAutoField(primary_key=True)
    definitionid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_gradingform_rubric_criteria'


class McGradingformRubricFillings(models.Model):
    id = models.BigAutoField(primary_key=True)
    instanceid = models.BigIntegerField()
    criterionid = models.BigIntegerField()
    levelid = models.BigIntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    remarkformat = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_gradingform_rubric_fillings'
        unique_together = (('instanceid', 'criterionid'),)


class McGradingformRubricLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    criterionid = models.BigIntegerField()
    score = models.DecimalField(max_digits=10, decimal_places=5)
    definition = models.TextField(blank=True, null=True)
    definitionformat = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_gradingform_rubric_levels'


class McGroupings(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    configdata = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_groupings'


class McGroupingsGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupingid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    timeadded = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_groupings_groups'


class McGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    idnumber = models.CharField(max_length=100)
    name = models.CharField(max_length=254)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    enrolmentkey = models.CharField(max_length=50, blank=True, null=True)
    picture = models.BigIntegerField()
    hidepicture = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_groups'


class McGroupsMembers(models.Model):
    id = models.BigAutoField(primary_key=True)
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timeadded = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_groups_members'


class McImscp(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    revision = models.BigIntegerField()
    keepold = models.BigIntegerField()
    structure = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_imscp'


class McLabel(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_label'


class McLesson(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    practice = models.SmallIntegerField()
    modattempts = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    dependency = models.BigIntegerField()
    conditions = models.TextField()
    grade = models.BigIntegerField()
    custom = models.SmallIntegerField()
    ongoing = models.SmallIntegerField()
    usemaxgrade = models.SmallIntegerField()
    maxanswers = models.SmallIntegerField()
    maxattempts = models.SmallIntegerField()
    review = models.SmallIntegerField()
    nextpagedefault = models.SmallIntegerField()
    feedback = models.SmallIntegerField()
    minquestions = models.SmallIntegerField()
    maxpages = models.SmallIntegerField()
    timelimit = models.BigIntegerField()
    retake = models.SmallIntegerField()
    activitylink = models.BigIntegerField()
    mediafile = models.CharField(max_length=255)
    mediaheight = models.BigIntegerField()
    mediawidth = models.BigIntegerField()
    mediaclose = models.SmallIntegerField()
    slideshow = models.SmallIntegerField()
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    bgcolor = models.CharField(max_length=7)
    displayleft = models.SmallIntegerField()
    displayleftif = models.SmallIntegerField()
    progressbar = models.SmallIntegerField()
    highscores = models.SmallIntegerField()
    maxhighscores = models.BigIntegerField()
    available = models.BigIntegerField()
    deadline = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionendreached = models.IntegerField(blank=True, null=True)
    completiontimespent = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_lesson'


class McLessonAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    jumpto = models.BigIntegerField()
    grade = models.SmallIntegerField()
    score = models.BigIntegerField()
    flags = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    answer = models.TextField(blank=True, null=True)
    answerformat = models.IntegerField()
    response = models.TextField(blank=True, null=True)
    responseformat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lesson_answers'


class McLessonAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    userid = models.BigIntegerField()
    answerid = models.BigIntegerField()
    retry = models.SmallIntegerField()
    correct = models.BigIntegerField()
    useranswer = models.TextField(blank=True, null=True)
    timeseen = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lesson_attempts'


class McLessonBranch(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    retry = models.BigIntegerField()
    flag = models.SmallIntegerField()
    timeseen = models.BigIntegerField()
    nextpageid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lesson_branch'


class McLessonGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.FloatField()
    late = models.SmallIntegerField()
    completed = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lesson_grades'


class McLessonHighScores(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    gradeid = models.BigIntegerField()
    nickname = models.CharField(max_length=5)

    class Meta:
        managed = False
        db_table = 'mc_lesson_high_scores'


class McLessonOverrides(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    groupid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    available = models.BigIntegerField(blank=True, null=True)
    deadline = models.BigIntegerField(blank=True, null=True)
    timelimit = models.BigIntegerField(blank=True, null=True)
    review = models.SmallIntegerField(blank=True, null=True)
    maxattempts = models.SmallIntegerField(blank=True, null=True)
    retake = models.SmallIntegerField(blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_lesson_overrides'


class McLessonPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    prevpageid = models.BigIntegerField()
    nextpageid = models.BigIntegerField()
    qtype = models.SmallIntegerField()
    qoption = models.SmallIntegerField()
    layout = models.SmallIntegerField()
    display = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    title = models.CharField(max_length=255)
    contents = models.TextField()
    contentsformat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lesson_pages'


class McLessonTimer(models.Model):
    id = models.BigAutoField(primary_key=True)
    lessonid = models.BigIntegerField()
    userid = models.BigIntegerField()
    starttime = models.BigIntegerField()
    lessontime = models.BigIntegerField()
    completed = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_lesson_timer'


class McLicense(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=255, blank=True, null=True)
    fullname = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=255, blank=True, null=True)
    enabled = models.IntegerField()
    version = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_license'


class McLockDb(models.Model):
    id = models.BigAutoField(primary_key=True)
    resourcekey = models.CharField(unique=True, max_length=255)
    expires = models.BigIntegerField(blank=True, null=True)
    owner = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_lock_db'


class McLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    time = models.BigIntegerField()
    userid = models.BigIntegerField()
    ip = models.CharField(max_length=45)
    course = models.BigIntegerField()
    module = models.CharField(max_length=20)
    cmid = models.BigIntegerField()
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_log'


class McLogDisplay(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.CharField(max_length=20)
    action = models.CharField(max_length=40)
    mtable = models.CharField(max_length=30)
    field = models.CharField(max_length=200)
    component = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'mc_log_display'
        unique_together = (('module', 'action'),)


class McLogQueries(models.Model):
    id = models.BigAutoField(primary_key=True)
    qtype = models.IntegerField()
    sqltext = models.TextField()
    sqlparams = models.TextField(blank=True, null=True)
    error = models.IntegerField()
    info = models.TextField(blank=True, null=True)
    backtrace = models.TextField(blank=True, null=True)
    exectime = models.DecimalField(max_digits=10, decimal_places=5)
    timelogged = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_log_queries'


class McLogstoreStandardLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=255)
    component = models.CharField(max_length=100)
    action = models.CharField(max_length=100)
    target = models.CharField(max_length=100)
    objecttable = models.CharField(max_length=50, blank=True, null=True)
    objectid = models.BigIntegerField(blank=True, null=True)
    crud = models.CharField(max_length=1)
    edulevel = models.IntegerField()
    contextid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()
    contextinstanceid = models.BigIntegerField()
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField(blank=True, null=True)
    relateduserid = models.BigIntegerField(blank=True, null=True)
    anonymous = models.IntegerField()
    other = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    origin = models.CharField(max_length=10, blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    realuserid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_logstore_standard_log'


class McLti(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    typeid = models.BigIntegerField(blank=True, null=True)
    toolurl = models.TextField()
    securetoolurl = models.TextField(blank=True, null=True)
    instructorchoicesendname = models.IntegerField(blank=True, null=True)
    instructorchoicesendemailaddr = models.IntegerField(blank=True, null=True)
    instructorchoiceallowroster = models.IntegerField(blank=True, null=True)
    instructorchoiceallowsetting = models.IntegerField(blank=True, null=True)
    instructorcustomparameters = models.CharField(max_length=255, blank=True, null=True)
    instructorchoiceacceptgrades = models.IntegerField(blank=True, null=True)
    grade = models.BigIntegerField()
    launchcontainer = models.IntegerField()
    resourcekey = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    debuglaunch = models.IntegerField()
    showtitlelaunch = models.IntegerField()
    showdescriptionlaunch = models.IntegerField()
    servicesalt = models.CharField(max_length=40, blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    secureicon = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_lti'


class McLtiSubmission(models.Model):
    id = models.BigAutoField(primary_key=True)
    ltiid = models.BigIntegerField()
    userid = models.BigIntegerField()
    datesubmitted = models.BigIntegerField()
    dateupdated = models.BigIntegerField()
    gradepercent = models.DecimalField(max_digits=10, decimal_places=5)
    originalgrade = models.DecimalField(max_digits=10, decimal_places=5)
    launchid = models.BigIntegerField()
    state = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lti_submission'


class McLtiToolProxies(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    regurl = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    guid = models.CharField(unique=True, max_length=255, blank=True, null=True)
    secret = models.CharField(max_length=255, blank=True, null=True)
    vendorcode = models.CharField(max_length=255, blank=True, null=True)
    capabilityoffered = models.TextField()
    serviceoffered = models.TextField()
    toolproxy = models.TextField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lti_tool_proxies'


class McLtiToolSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    toolproxyid = models.BigIntegerField()
    course = models.BigIntegerField(blank=True, null=True)
    coursemoduleid = models.BigIntegerField(blank=True, null=True)
    settings = models.TextField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lti_tool_settings'


class McLtiTypes(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    baseurl = models.TextField()
    tooldomain = models.CharField(max_length=255)
    state = models.IntegerField()
    course = models.BigIntegerField()
    coursevisible = models.IntegerField()
    toolproxyid = models.BigIntegerField(blank=True, null=True)
    enabledcapability = models.TextField(blank=True, null=True)
    parameter = models.TextField(blank=True, null=True)
    icon = models.TextField(blank=True, null=True)
    secureicon = models.TextField(blank=True, null=True)
    createdby = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_lti_types'


class McLtiTypesConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    typeid = models.BigIntegerField()
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_lti_types_config'


class McMessage(models.Model):
    id = models.BigAutoField(primary_key=True)
    useridfrom = models.BigIntegerField()
    useridto = models.BigIntegerField()
    subject = models.TextField(blank=True, null=True)
    fullmessage = models.TextField(blank=True, null=True)
    fullmessageformat = models.SmallIntegerField(blank=True, null=True)
    fullmessagehtml = models.TextField(blank=True, null=True)
    smallmessage = models.TextField(blank=True, null=True)
    notification = models.IntegerField(blank=True, null=True)
    contexturl = models.TextField(blank=True, null=True)
    contexturlname = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_message'


class McMessageAirnotifierDevices(models.Model):
    id = models.BigAutoField(primary_key=True)
    userdeviceid = models.BigIntegerField(unique=True)
    enable = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_message_airnotifier_devices'


class McMessageContacts(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    contactid = models.BigIntegerField()
    blocked = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_message_contacts'
        unique_together = (('userid', 'contactid'),)


class McMessageProcessors(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=166)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_message_processors'


class McMessageProviders(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    component = models.CharField(max_length=200)
    capability = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_message_providers'
        unique_together = (('component', 'name'),)


class McMessageRead(models.Model):
    id = models.BigAutoField(primary_key=True)
    useridfrom = models.BigIntegerField()
    useridto = models.BigIntegerField()
    subject = models.TextField(blank=True, null=True)
    fullmessage = models.TextField(blank=True, null=True)
    fullmessageformat = models.SmallIntegerField(blank=True, null=True)
    fullmessagehtml = models.TextField(blank=True, null=True)
    smallmessage = models.TextField(blank=True, null=True)
    notification = models.IntegerField(blank=True, null=True)
    contexturl = models.TextField(blank=True, null=True)
    contexturlname = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timeread = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_message_read'


class McMessageWorking(models.Model):
    id = models.BigAutoField(primary_key=True)
    unreadmessageid = models.BigIntegerField()
    processorid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_message_working'


class McMessageinboundDatakeys(models.Model):
    id = models.BigAutoField(primary_key=True)
    handler = models.BigIntegerField()
    datavalue = models.BigIntegerField()
    datakey = models.CharField(max_length=64, blank=True, null=True)
    timecreated = models.BigIntegerField()
    expires = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_messageinbound_datakeys'
        unique_together = (('handler', 'datavalue'),)


class McMessageinboundHandlers(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=100)
    classname = models.CharField(unique=True, max_length=255)
    defaultexpiration = models.BigIntegerField()
    validateaddress = models.IntegerField()
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_messageinbound_handlers'


class McMessageinboundMessagelist(models.Model):
    id = models.BigAutoField(primary_key=True)
    messageid = models.TextField()
    userid = models.BigIntegerField()
    address = models.TextField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_messageinbound_messagelist'


class McMnetApplication(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    display_name = models.CharField(max_length=50)
    xmlrpc_server_url = models.CharField(max_length=255)
    sso_land_url = models.CharField(max_length=255)
    sso_jump_url = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_mnet_application'


class McMnetHost(models.Model):
    id = models.BigAutoField(primary_key=True)
    deleted = models.IntegerField()
    wwwroot = models.CharField(max_length=255)
    ip_address = models.CharField(max_length=45)
    name = models.CharField(max_length=80)
    public_key = models.TextField()
    public_key_expires = models.BigIntegerField()
    transport = models.IntegerField()
    portno = models.IntegerField()
    last_connect_time = models.BigIntegerField()
    last_log_id = models.BigIntegerField()
    force_theme = models.IntegerField()
    theme = models.CharField(max_length=100, blank=True, null=True)
    applicationid = models.BigIntegerField()
    sslverification = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_host'


class McMnetHost2Service(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    serviceid = models.BigIntegerField()
    publish = models.IntegerField()
    subscribe = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_host2service'
        unique_together = (('hostid', 'serviceid'),)


class McMnetLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    remoteid = models.BigIntegerField()
    time = models.BigIntegerField()
    userid = models.BigIntegerField()
    ip = models.CharField(max_length=45)
    course = models.BigIntegerField()
    coursename = models.CharField(max_length=40)
    module = models.CharField(max_length=20)
    cmid = models.BigIntegerField()
    action = models.CharField(max_length=40)
    url = models.CharField(max_length=100)
    info = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_mnet_log'


class McMnetRemoteRpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    functionname = models.CharField(max_length=40)
    xmlrpcpath = models.CharField(max_length=80)
    plugintype = models.CharField(max_length=20)
    pluginname = models.CharField(max_length=20)
    enabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_remote_rpc'


class McMnetRemoteService2Rpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    serviceid = models.BigIntegerField()
    rpcid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_remote_service2rpc'
        unique_together = (('rpcid', 'serviceid'),)


class McMnetRpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    functionname = models.CharField(max_length=40)
    xmlrpcpath = models.CharField(max_length=80)
    plugintype = models.CharField(max_length=20)
    pluginname = models.CharField(max_length=20)
    enabled = models.IntegerField()
    help = models.TextField()
    profile = models.TextField()
    filename = models.CharField(max_length=100)
    classname = models.CharField(max_length=150, blank=True, null=True)
    static = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_mnet_rpc'


class McMnetService(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=40)
    apiversion = models.CharField(max_length=10)
    offer = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_service'


class McMnetService2Rpc(models.Model):
    id = models.BigAutoField(primary_key=True)
    serviceid = models.BigIntegerField()
    rpcid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_service2rpc'
        unique_together = (('rpcid', 'serviceid'),)


class McMnetSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    token = models.CharField(unique=True, max_length=40)
    mnethostid = models.BigIntegerField()
    useragent = models.CharField(max_length=40)
    confirm_timeout = models.BigIntegerField()
    session_id = models.CharField(max_length=40)
    expires = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_mnet_session'


class McMnetSsoAccessControl(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=100)
    mnet_host_id = models.BigIntegerField()
    accessctrl = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mc_mnet_sso_access_control'
        unique_together = (('mnet_host_id', 'username'),)


class McMnetserviceEnrolCourses(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    remoteid = models.BigIntegerField()
    categoryid = models.BigIntegerField()
    categoryname = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()
    fullname = models.CharField(max_length=254)
    shortname = models.CharField(max_length=100)
    idnumber = models.CharField(max_length=100)
    summary = models.TextField()
    summaryformat = models.SmallIntegerField(blank=True, null=True)
    startdate = models.BigIntegerField()
    roleid = models.BigIntegerField()
    rolename = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_mnetservice_enrol_courses'
        unique_together = (('hostid', 'remoteid'),)


class McMnetserviceEnrolEnrolments(models.Model):
    id = models.BigAutoField(primary_key=True)
    hostid = models.BigIntegerField()
    userid = models.BigIntegerField()
    remotecourseid = models.BigIntegerField()
    rolename = models.CharField(max_length=255)
    enroltime = models.BigIntegerField()
    enroltype = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'mc_mnetservice_enrol_enrolments'


class McModules(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20)
    cron = models.BigIntegerField()
    lastcron = models.BigIntegerField()
    search = models.CharField(max_length=255)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_modules'


class McMyPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    private = models.IntegerField()
    sortorder = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_my_pages'


class McPage(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    content = models.TextField(blank=True, null=True)
    contentformat = models.SmallIntegerField()
    legacyfiles = models.SmallIntegerField()
    legacyfileslast = models.BigIntegerField(blank=True, null=True)
    display = models.SmallIntegerField()
    displayoptions = models.TextField(blank=True, null=True)
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_page'


class McPortfolioInstance(models.Model):
    id = models.BigAutoField(primary_key=True)
    plugin = models.CharField(max_length=50)
    name = models.CharField(max_length=255)
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_portfolio_instance'


class McPortfolioInstanceConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_portfolio_instance_config'


class McPortfolioInstanceUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    instance = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_portfolio_instance_user'


class McPortfolioLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    time = models.BigIntegerField()
    portfolio = models.BigIntegerField()
    caller_class = models.CharField(max_length=150)
    caller_file = models.CharField(max_length=255)
    caller_component = models.CharField(max_length=255, blank=True, null=True)
    caller_sha1 = models.CharField(max_length=255)
    tempdataid = models.BigIntegerField()
    returnurl = models.CharField(max_length=255)
    continueurl = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_portfolio_log'


class McPortfolioMaharaQueue(models.Model):
    id = models.BigAutoField(primary_key=True)
    transferid = models.BigIntegerField()
    token = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mc_portfolio_mahara_queue'


class McPortfolioTempdata(models.Model):
    id = models.BigAutoField(primary_key=True)
    data = models.TextField(blank=True, null=True)
    expirytime = models.BigIntegerField()
    userid = models.BigIntegerField()
    instance = models.BigIntegerField(blank=True, null=True)
    queued = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_portfolio_tempdata'


class McPost(models.Model):
    id = models.BigAutoField(primary_key=True)
    module = models.CharField(max_length=20)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    moduleid = models.BigIntegerField()
    coursemoduleid = models.BigIntegerField()
    subject = models.CharField(max_length=128)
    summary = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    uniquehash = models.CharField(max_length=255)
    rating = models.BigIntegerField()
    format = models.BigIntegerField()
    summaryformat = models.IntegerField()
    attachment = models.CharField(max_length=100, blank=True, null=True)
    publishstate = models.CharField(max_length=20)
    lastmodified = models.BigIntegerField()
    created = models.BigIntegerField()
    usermodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_post'
        unique_together = (('id', 'userid'),)


class McProfiling(models.Model):
    id = models.BigAutoField(primary_key=True)
    runid = models.CharField(unique=True, max_length=32)
    url = models.CharField(max_length=255)
    data = models.TextField()
    totalexecutiontime = models.BigIntegerField()
    totalcputime = models.BigIntegerField()
    totalcalls = models.BigIntegerField()
    totalmemory = models.BigIntegerField()
    runreference = models.IntegerField()
    runcomment = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_profiling'


class McQtypeEssayOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    responseformat = models.CharField(max_length=16)
    responserequired = models.IntegerField()
    responsefieldlines = models.SmallIntegerField()
    attachments = models.SmallIntegerField()
    attachmentsrequired = models.SmallIntegerField()
    graderinfo = models.TextField(blank=True, null=True)
    graderinfoformat = models.SmallIntegerField()
    responsetemplate = models.TextField(blank=True, null=True)
    responsetemplateformat = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_qtype_essay_options'


class McQtypeMatchOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.IntegerField()
    shownumcorrect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_qtype_match_options'


class McQtypeMatchSubquestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    questiontext = models.TextField()
    questiontextformat = models.IntegerField()
    answertext = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_qtype_match_subquestions'


class McQtypeMultichoiceOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    layout = models.SmallIntegerField()
    single = models.SmallIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.IntegerField()
    answernumbering = models.CharField(max_length=10)
    shownumcorrect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_qtype_multichoice_options'


class McQtypeRandomsamatchOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    choose = models.BigIntegerField()
    subcats = models.IntegerField()
    correctfeedback = models.TextField()
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField()
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField()
    incorrectfeedbackformat = models.IntegerField()
    shownumcorrect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_qtype_randomsamatch_options'


class McQtypeShortanswerOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField(unique=True)
    usecase = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_qtype_shortanswer_options'


class McQuestion(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    parent = models.BigIntegerField()
    name = models.CharField(max_length=255)
    questiontext = models.TextField()
    questiontextformat = models.IntegerField()
    generalfeedback = models.TextField()
    generalfeedbackformat = models.IntegerField()
    defaultmark = models.DecimalField(max_digits=12, decimal_places=7)
    penalty = models.DecimalField(max_digits=12, decimal_places=7)
    qtype = models.CharField(max_length=20)
    length = models.BigIntegerField()
    stamp = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    hidden = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    createdby = models.BigIntegerField(blank=True, null=True)
    modifiedby = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_question'


class McQuestionAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.TextField()
    answerformat = models.IntegerField()
    fraction = models.DecimalField(max_digits=12, decimal_places=7)
    feedback = models.TextField()
    feedbackformat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_answers'


class McQuestionAttemptStepData(models.Model):
    id = models.BigAutoField(primary_key=True)
    attemptstepid = models.BigIntegerField()
    name = models.CharField(max_length=32)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_question_attempt_step_data'
        unique_together = (('attemptstepid', 'name'),)


class McQuestionAttemptSteps(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionattemptid = models.BigIntegerField()
    sequencenumber = models.BigIntegerField()
    state = models.CharField(max_length=13)
    fraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_question_attempt_steps'
        unique_together = (('questionattemptid', 'sequencenumber'),)


class McQuestionAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionusageid = models.BigIntegerField()
    slot = models.BigIntegerField()
    behaviour = models.CharField(max_length=32)
    questionid = models.BigIntegerField()
    variant = models.BigIntegerField()
    maxmark = models.DecimalField(max_digits=12, decimal_places=7)
    minfraction = models.DecimalField(max_digits=12, decimal_places=7)
    maxfraction = models.DecimalField(max_digits=12, decimal_places=7)
    flagged = models.IntegerField()
    questionsummary = models.TextField(blank=True, null=True)
    rightanswer = models.TextField(blank=True, null=True)
    responsesummary = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_attempts'
        unique_together = (('questionusageid', 'slot'),)


class McQuestionCalculated(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.BigIntegerField()
    tolerance = models.CharField(max_length=20)
    tolerancetype = models.BigIntegerField()
    correctanswerlength = models.BigIntegerField()
    correctanswerformat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_calculated'


class McQuestionCalculatedOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    synchronize = models.IntegerField()
    single = models.SmallIntegerField()
    shuffleanswers = models.SmallIntegerField()
    correctfeedback = models.TextField(blank=True, null=True)
    correctfeedbackformat = models.IntegerField()
    partiallycorrectfeedback = models.TextField(blank=True, null=True)
    partiallycorrectfeedbackformat = models.IntegerField()
    incorrectfeedback = models.TextField(blank=True, null=True)
    incorrectfeedbackformat = models.IntegerField()
    answernumbering = models.CharField(max_length=10)
    shownumcorrect = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_calculated_options'


class McQuestionCategories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contextid = models.BigIntegerField()
    info = models.TextField()
    infoformat = models.IntegerField()
    stamp = models.CharField(max_length=255)
    parent = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_categories'


class McQuestionDatasetDefinitions(models.Model):
    id = models.BigAutoField(primary_key=True)
    category = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.BigIntegerField()
    options = models.CharField(max_length=255)
    itemcount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_dataset_definitions'


class McQuestionDatasetItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    definition = models.BigIntegerField()
    itemnumber = models.BigIntegerField()
    value = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_question_dataset_items'


class McQuestionDatasets(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    datasetdefinition = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_datasets'


class McQuestionHints(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionid = models.BigIntegerField()
    hint = models.TextField()
    hintformat = models.SmallIntegerField()
    shownumcorrect = models.IntegerField(blank=True, null=True)
    clearwrong = models.IntegerField(blank=True, null=True)
    options = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_question_hints'


class McQuestionMultianswer(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    sequence = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_question_multianswer'


class McQuestionNumerical(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    answer = models.BigIntegerField()
    tolerance = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_question_numerical'


class McQuestionNumericalOptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    showunits = models.SmallIntegerField()
    unitsleft = models.SmallIntegerField()
    unitgradingtype = models.SmallIntegerField()
    unitpenalty = models.DecimalField(max_digits=12, decimal_places=7)

    class Meta:
        managed = False
        db_table = 'mc_question_numerical_options'


class McQuestionNumericalUnits(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    multiplier = models.DecimalField(max_digits=40, decimal_places=20)
    unit = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'mc_question_numerical_units'
        unique_together = (('question', 'unit'),)


class McQuestionResponseAnalysis(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=40)
    whichtries = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    questionid = models.BigIntegerField()
    variant = models.BigIntegerField(blank=True, null=True)
    subqid = models.CharField(max_length=100)
    aid = models.CharField(max_length=100, blank=True, null=True)
    response = models.TextField(blank=True, null=True)
    credit = models.DecimalField(max_digits=15, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mc_question_response_analysis'


class McQuestionResponseCount(models.Model):
    id = models.BigAutoField(primary_key=True)
    analysisid = models.BigIntegerField()
    try_field = models.BigIntegerField(db_column='try')  # Field renamed because it was a Python reserved word.
    rcount = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_response_count'


class McQuestionStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=40)
    timemodified = models.BigIntegerField()
    questionid = models.BigIntegerField()
    slot = models.BigIntegerField(blank=True, null=True)
    subquestion = models.SmallIntegerField()
    variant = models.BigIntegerField(blank=True, null=True)
    s = models.BigIntegerField()
    effectiveweight = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    negcovar = models.IntegerField()
    discriminationindex = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    discriminativeefficiency = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    sd = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    facility = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    subquestions = models.TextField(blank=True, null=True)
    maxmark = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    positions = models.TextField(blank=True, null=True)
    randomguessscore = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_question_statistics'


class McQuestionTruefalse(models.Model):
    id = models.BigAutoField(primary_key=True)
    question = models.BigIntegerField()
    trueanswer = models.BigIntegerField()
    falseanswer = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_question_truefalse'


class McQuestionUsages(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=255)
    preferredbehaviour = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'mc_question_usages'


class McQuiz(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timelimit = models.BigIntegerField()
    overduehandling = models.CharField(max_length=16)
    graceperiod = models.BigIntegerField()
    preferredbehaviour = models.CharField(max_length=32)
    canredoquestions = models.SmallIntegerField()
    attempts = models.IntegerField()
    attemptonlast = models.SmallIntegerField()
    grademethod = models.SmallIntegerField()
    decimalpoints = models.SmallIntegerField()
    questiondecimalpoints = models.SmallIntegerField()
    reviewattempt = models.IntegerField()
    reviewcorrectness = models.IntegerField()
    reviewmarks = models.IntegerField()
    reviewspecificfeedback = models.IntegerField()
    reviewgeneralfeedback = models.IntegerField()
    reviewrightanswer = models.IntegerField()
    reviewoverallfeedback = models.IntegerField()
    questionsperpage = models.BigIntegerField()
    navmethod = models.CharField(max_length=16)
    shuffleanswers = models.SmallIntegerField()
    sumgrades = models.DecimalField(max_digits=10, decimal_places=5)
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    password = models.CharField(max_length=255)
    subnet = models.CharField(max_length=255)
    browsersecurity = models.CharField(max_length=32)
    delay1 = models.BigIntegerField()
    delay2 = models.BigIntegerField()
    showuserpicture = models.SmallIntegerField()
    showblocks = models.SmallIntegerField()
    completionattemptsexhausted = models.IntegerField(blank=True, null=True)
    completionpass = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_quiz'


class McQuizAttempts(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.BigIntegerField()
    userid = models.BigIntegerField()
    attempt = models.IntegerField()
    uniqueid = models.BigIntegerField(unique=True)
    layout = models.TextField()
    currentpage = models.BigIntegerField()
    preview = models.SmallIntegerField()
    state = models.CharField(max_length=16)
    timestart = models.BigIntegerField()
    timefinish = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    timecheckstate = models.BigIntegerField(blank=True, null=True)
    sumgrades = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_quiz_attempts'
        unique_together = (('quiz', 'userid', 'attempt'),)


class McQuizFeedback(models.Model):
    id = models.BigAutoField(primary_key=True)
    quizid = models.BigIntegerField()
    feedbacktext = models.TextField()
    feedbacktextformat = models.IntegerField()
    mingrade = models.DecimalField(max_digits=10, decimal_places=5)
    maxgrade = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mc_quiz_feedback'


class McQuizGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.BigIntegerField()
    userid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_quiz_grades'


class McQuizOverrides(models.Model):
    id = models.BigAutoField(primary_key=True)
    quiz = models.BigIntegerField()
    groupid = models.BigIntegerField(blank=True, null=True)
    userid = models.BigIntegerField(blank=True, null=True)
    timeopen = models.BigIntegerField(blank=True, null=True)
    timeclose = models.BigIntegerField(blank=True, null=True)
    timelimit = models.BigIntegerField(blank=True, null=True)
    attempts = models.IntegerField(blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_quiz_overrides'


class McQuizOverviewRegrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    questionusageid = models.BigIntegerField()
    slot = models.BigIntegerField()
    newfraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    oldfraction = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    regraded = models.SmallIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_quiz_overview_regrades'


class McQuizReports(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    displayorder = models.BigIntegerField()
    capability = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_quiz_reports'


class McQuizSections(models.Model):
    id = models.BigAutoField(primary_key=True)
    quizid = models.BigIntegerField()
    firstslot = models.BigIntegerField()
    heading = models.CharField(max_length=1333, blank=True, null=True)
    shufflequestions = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_quiz_sections'
        unique_together = (('quizid', 'firstslot'),)


class McQuizSlots(models.Model):
    id = models.BigAutoField(primary_key=True)
    slot = models.BigIntegerField()
    quizid = models.BigIntegerField()
    page = models.BigIntegerField()
    requireprevious = models.SmallIntegerField()
    questionid = models.BigIntegerField()
    maxmark = models.DecimalField(max_digits=12, decimal_places=7)

    class Meta:
        managed = False
        db_table = 'mc_quiz_slots'
        unique_together = (('quizid', 'slot'),)


class McQuizStatistics(models.Model):
    id = models.BigAutoField(primary_key=True)
    hashcode = models.CharField(max_length=40)
    whichattempts = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    firstattemptscount = models.BigIntegerField()
    highestattemptscount = models.BigIntegerField()
    lastattemptscount = models.BigIntegerField()
    allattemptscount = models.BigIntegerField()
    firstattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    highestattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    lastattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    allattemptsavg = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    median = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    standarddeviation = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    skewness = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    kurtosis = models.DecimalField(max_digits=15, decimal_places=5, blank=True, null=True)
    cic = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    errorratio = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    standarderror = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_quiz_statistics'


class McRating(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    ratingarea = models.CharField(max_length=50)
    itemid = models.BigIntegerField()
    scaleid = models.BigIntegerField()
    rating = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_rating'


class McRegistrationHubs(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(max_length=255)
    hubname = models.CharField(max_length=255)
    huburl = models.CharField(max_length=255)
    confirmed = models.IntegerField()
    secret = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_registration_hubs'


class McRepository(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.CharField(max_length=255)
    visible = models.IntegerField(blank=True, null=True)
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_repository'


class McRepositoryInstanceConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    instanceid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_repository_instance_config'


class McRepositoryInstances(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    typeid = models.BigIntegerField()
    userid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    username = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    readonly = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_repository_instances'


class McResource(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    tobemigrated = models.SmallIntegerField()
    legacyfiles = models.SmallIntegerField()
    legacyfileslast = models.BigIntegerField(blank=True, null=True)
    display = models.SmallIntegerField()
    displayoptions = models.TextField(blank=True, null=True)
    filterfiles = models.SmallIntegerField()
    revision = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_resource'


class McResourceOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=30)
    reference = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    alltext = models.TextField()
    popup = models.TextField()
    options = models.CharField(max_length=255)
    timemodified = models.BigIntegerField()
    oldid = models.BigIntegerField(unique=True)
    cmid = models.BigIntegerField(blank=True, null=True)
    newmodule = models.CharField(max_length=50, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)
    migrated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_resource_old'


class McRole(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    shortname = models.CharField(unique=True, max_length=100)
    description = models.TextField()
    sortorder = models.BigIntegerField(unique=True)
    archetype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mc_role'


class McRoleAllowAssign(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    allowassign = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_allow_assign'
        unique_together = (('roleid', 'allowassign'),)


class McRoleAllowOverride(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    allowoverride = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_allow_override'
        unique_together = (('roleid', 'allowoverride'),)


class McRoleAllowSwitch(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    allowswitch = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_allow_switch'
        unique_together = (('roleid', 'allowswitch'),)


class McRoleAssignments(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    component = models.CharField(max_length=100)
    itemid = models.BigIntegerField()
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_assignments'


class McRoleCapabilities(models.Model):
    id = models.BigAutoField(primary_key=True)
    contextid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    capability = models.CharField(max_length=255)
    permission = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    modifierid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_capabilities'
        unique_together = (('roleid', 'contextid', 'capability'),)


class McRoleContextLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_context_levels'
        unique_together = (('contextlevel', 'roleid'),)


class McRoleNames(models.Model):
    id = models.BigAutoField(primary_key=True)
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_role_names'
        unique_together = (('roleid', 'contextid'),)


class McRoleSortorder(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    contextid = models.BigIntegerField()
    sortoder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_role_sortorder'
        unique_together = (('userid', 'roleid', 'contextid'),)


class McScale(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()
    descriptionformat = models.IntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_scale'


class McScaleHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    action = models.BigIntegerField()
    oldid = models.BigIntegerField()
    source = models.CharField(max_length=255, blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    loggeduser = models.BigIntegerField(blank=True, null=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scale = models.TextField()
    description = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_scale_history'


class McScorm(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    scormtype = models.CharField(max_length=50)
    reference = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    version = models.CharField(max_length=9)
    maxgrade = models.FloatField()
    grademethod = models.IntegerField()
    whatgrade = models.BigIntegerField()
    maxattempt = models.BigIntegerField()
    forcecompleted = models.IntegerField()
    forcenewattempt = models.IntegerField()
    lastattemptlock = models.IntegerField()
    displayattemptstatus = models.IntegerField()
    displaycoursestructure = models.IntegerField()
    updatefreq = models.IntegerField()
    sha1hash = models.CharField(max_length=40, blank=True, null=True)
    md5hash = models.CharField(max_length=32)
    revision = models.BigIntegerField()
    launch = models.BigIntegerField()
    skipview = models.IntegerField()
    hidebrowse = models.IntegerField()
    hidetoc = models.IntegerField()
    nav = models.IntegerField()
    navpositionleft = models.BigIntegerField(blank=True, null=True)
    navpositiontop = models.BigIntegerField(blank=True, null=True)
    auto = models.IntegerField()
    popup = models.IntegerField()
    options = models.CharField(max_length=255)
    width = models.BigIntegerField()
    height = models.BigIntegerField()
    timeopen = models.BigIntegerField()
    timeclose = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    completionstatusrequired = models.IntegerField(blank=True, null=True)
    completionscorerequired = models.IntegerField(blank=True, null=True)
    displayactivityname = models.SmallIntegerField()
    autocommit = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_scorm'


class McScormAiccSession(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    scormid = models.BigIntegerField()
    hacpsession = models.CharField(max_length=255)
    scoid = models.BigIntegerField(blank=True, null=True)
    scormmode = models.CharField(max_length=50, blank=True, null=True)
    scormstatus = models.CharField(max_length=255, blank=True, null=True)
    attempt = models.BigIntegerField(blank=True, null=True)
    lessonstatus = models.CharField(max_length=255, blank=True, null=True)
    sessiontime = models.CharField(max_length=255, blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_scorm_aicc_session'


class McScormScoes(models.Model):
    id = models.BigAutoField(primary_key=True)
    scorm = models.BigIntegerField()
    manifest = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    parent = models.CharField(max_length=255)
    identifier = models.CharField(max_length=255)
    launch = models.TextField()
    scormtype = models.CharField(max_length=5)
    title = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_scorm_scoes'


class McScormScoesData(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_scorm_scoes_data'


class McScormScoesTrack(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    scormid = models.BigIntegerField()
    scoid = models.BigIntegerField()
    attempt = models.BigIntegerField()
    element = models.CharField(max_length=255)
    value = models.TextField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_scorm_scoes_track'
        unique_together = (('userid', 'scormid', 'scoid', 'attempt', 'element'),)


class McScormSeqMapinfo(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    objectiveid = models.BigIntegerField()
    targetobjectiveid = models.BigIntegerField()
    readsatisfiedstatus = models.IntegerField()
    readnormalizedmeasure = models.IntegerField()
    writesatisfiedstatus = models.IntegerField()
    writenormalizedmeasure = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_scorm_seq_mapinfo'
        unique_together = (('scoid', 'id', 'objectiveid'),)


class McScormSeqObjective(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    primaryobj = models.IntegerField()
    objectiveid = models.CharField(max_length=255)
    satisfiedbymeasure = models.IntegerField()
    minnormalizedmeasure = models.FloatField()

    class Meta:
        managed = False
        db_table = 'mc_scorm_seq_objective'
        unique_together = (('scoid', 'id'),)


class McScormSeqRolluprule(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    childactivityset = models.CharField(max_length=15)
    minimumcount = models.BigIntegerField()
    minimumpercent = models.FloatField()
    conditioncombination = models.CharField(max_length=3)
    action = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'mc_scorm_seq_rolluprule'
        unique_together = (('scoid', 'id'),)


class McScormSeqRolluprulecond(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    rollupruleid = models.BigIntegerField()
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'mc_scorm_seq_rolluprulecond'
        unique_together = (('scoid', 'rollupruleid', 'id'),)


class McScormSeqRulecond(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    ruleconditionsid = models.BigIntegerField()
    refrencedobjective = models.CharField(max_length=255)
    measurethreshold = models.FloatField()
    operator = models.CharField(max_length=5)
    cond = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mc_scorm_seq_rulecond'
        unique_together = (('id', 'scoid', 'ruleconditionsid'),)


class McScormSeqRuleconds(models.Model):
    id = models.BigAutoField(primary_key=True)
    scoid = models.BigIntegerField()
    conditioncombination = models.CharField(max_length=3)
    ruletype = models.IntegerField()
    action = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'mc_scorm_seq_ruleconds'
        unique_together = (('scoid', 'id'),)


class McSessions(models.Model):
    id = models.BigAutoField(primary_key=True)
    state = models.BigIntegerField()
    sid = models.CharField(unique=True, max_length=128)
    userid = models.BigIntegerField()
    sessdata = models.TextField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    firstip = models.CharField(max_length=45, blank=True, null=True)
    lastip = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_sessions'


class McStatsDaily(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_stats_daily'


class McStatsMonthly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_stats_monthly'


class McStatsUserDaily(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mc_stats_user_daily'


class McStatsUserMonthly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mc_stats_user_monthly'


class McStatsUserWeekly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    userid = models.BigIntegerField()
    roleid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    statsreads = models.BigIntegerField()
    statswrites = models.BigIntegerField()
    stattype = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'mc_stats_user_weekly'


class McStatsWeekly(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    timeend = models.BigIntegerField()
    roleid = models.BigIntegerField()
    stattype = models.CharField(max_length=20)
    stat1 = models.BigIntegerField()
    stat2 = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_stats_weekly'


class McSurvey(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    template = models.BigIntegerField()
    days = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField()
    introformat = models.SmallIntegerField()
    questions = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_survey'


class McSurveyAnalysis(models.Model):
    id = models.BigAutoField(primary_key=True)
    survey = models.BigIntegerField()
    userid = models.BigIntegerField()
    notes = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_survey_analysis'


class McSurveyAnswers(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    survey = models.BigIntegerField()
    question = models.BigIntegerField()
    time = models.BigIntegerField()
    answer1 = models.TextField()
    answer2 = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_survey_answers'


class McSurveyQuestions(models.Model):
    id = models.BigAutoField(primary_key=True)
    text = models.CharField(max_length=255)
    shorttext = models.CharField(max_length=30)
    multi = models.CharField(max_length=100)
    intro = models.CharField(max_length=50)
    type = models.SmallIntegerField()
    options = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_survey_questions'


class McTag(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(unique=True, max_length=255)
    rawname = models.CharField(max_length=255)
    tagtype = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    flag = models.SmallIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_tag'
        unique_together = (('id', 'name'),)


class McTagCorrelation(models.Model):
    id = models.BigAutoField(primary_key=True)
    tagid = models.BigIntegerField()
    correlatedtags = models.TextField()

    class Meta:
        managed = False
        db_table = 'mc_tag_correlation'


class McTagInstance(models.Model):
    id = models.BigAutoField(primary_key=True)
    tagid = models.BigIntegerField()
    component = models.CharField(max_length=100, blank=True, null=True)
    itemtype = models.CharField(max_length=255)
    itemid = models.BigIntegerField()
    contextid = models.BigIntegerField(blank=True, null=True)
    tiuserid = models.BigIntegerField()
    ordering = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_tag_instance'
        unique_together = (('itemtype', 'itemid', 'tagid', 'tiuserid'),)


class McTaskAdhoc(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=255)
    classname = models.CharField(max_length=255)
    nextruntime = models.BigIntegerField()
    faildelay = models.BigIntegerField(blank=True, null=True)
    customdata = models.TextField(blank=True, null=True)
    blocking = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_task_adhoc'


class McTaskScheduled(models.Model):
    id = models.BigAutoField(primary_key=True)
    component = models.CharField(max_length=255)
    classname = models.CharField(unique=True, max_length=255)
    lastruntime = models.BigIntegerField(blank=True, null=True)
    nextruntime = models.BigIntegerField(blank=True, null=True)
    blocking = models.IntegerField()
    minute = models.CharField(max_length=25)
    hour = models.CharField(max_length=25)
    day = models.CharField(max_length=25)
    month = models.CharField(max_length=25)
    dayofweek = models.CharField(max_length=25)
    faildelay = models.BigIntegerField(blank=True, null=True)
    customised = models.IntegerField()
    disabled = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_task_scheduled'


class McToolCustomlang(models.Model):
    id = models.BigAutoField(primary_key=True)
    lang = models.CharField(max_length=20)
    componentid = models.BigIntegerField()
    stringid = models.CharField(max_length=255)
    original = models.TextField()
    master = models.TextField(blank=True, null=True)
    local = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()
    timecustomized = models.BigIntegerField(blank=True, null=True)
    outdated = models.SmallIntegerField(blank=True, null=True)
    modified = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_tool_customlang'
        unique_together = (('lang', 'componentid', 'stringid'),)


class McToolCustomlangComponents(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_tool_customlang_components'


class McToolMonitorEvents(models.Model):
    id = models.BigAutoField(primary_key=True)
    eventname = models.CharField(max_length=254)
    contextid = models.BigIntegerField()
    contextlevel = models.BigIntegerField()
    contextinstanceid = models.BigIntegerField()
    link = models.CharField(max_length=254)
    courseid = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_tool_monitor_events'


class McToolMonitorHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    sid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timesent = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_tool_monitor_history'
        unique_together = (('sid', 'userid', 'timesent'),)


class McToolMonitorRules(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    name = models.CharField(max_length=254)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    plugin = models.CharField(max_length=254)
    eventname = models.CharField(max_length=254)
    template = models.TextField()
    templateformat = models.IntegerField()
    frequency = models.SmallIntegerField()
    timewindow = models.IntegerField()
    timemodified = models.BigIntegerField()
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_tool_monitor_rules'


class McToolMonitorSubscriptions(models.Model):
    id = models.BigAutoField(primary_key=True)
    courseid = models.BigIntegerField()
    ruleid = models.BigIntegerField()
    cmid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    lastnotificationsent = models.BigIntegerField()
    inactivedate = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_tool_monitor_subscriptions'


class McUpgradeLog(models.Model):
    id = models.BigAutoField(primary_key=True)
    type = models.BigIntegerField()
    plugin = models.CharField(max_length=100, blank=True, null=True)
    version = models.CharField(max_length=100, blank=True, null=True)
    targetversion = models.CharField(max_length=100, blank=True, null=True)
    info = models.CharField(max_length=255)
    details = models.TextField(blank=True, null=True)
    backtrace = models.TextField(blank=True, null=True)
    userid = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_upgrade_log'


class McUrl(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    externalurl = models.TextField()
    display = models.SmallIntegerField()
    displayoptions = models.TextField(blank=True, null=True)
    parameters = models.TextField(blank=True, null=True)
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_url'


class McUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    auth = models.CharField(max_length=20)
    confirmed = models.IntegerField()
    policyagreed = models.IntegerField()
    deleted = models.IntegerField()
    suspended = models.IntegerField()
    mnethostid = models.BigIntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    idnumber = models.CharField(max_length=255)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    emailstop = models.IntegerField()
    icq = models.CharField(max_length=15)
    skype = models.CharField(max_length=50)
    yahoo = models.CharField(max_length=50)
    aim = models.CharField(max_length=50)
    msn = models.CharField(max_length=50)
    phone1 = models.CharField(max_length=20)
    phone2 = models.CharField(max_length=20)
    institution = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=120)
    country = models.CharField(max_length=2)
    lang = models.CharField(max_length=30)
    calendartype = models.CharField(max_length=30)
    theme = models.CharField(max_length=50)
    timezone = models.CharField(max_length=100)
    firstaccess = models.BigIntegerField()
    lastaccess = models.BigIntegerField()
    lastlogin = models.BigIntegerField()
    currentlogin = models.BigIntegerField()
    lastip = models.CharField(max_length=45)
    secret = models.CharField(max_length=15)
    picture = models.BigIntegerField()
    url = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    mailformat = models.IntegerField()
    maildigest = models.IntegerField()
    maildisplay = models.IntegerField()
    autosubscribe = models.IntegerField()
    trackforums = models.IntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    trustbitmask = models.BigIntegerField()
    imagealt = models.CharField(max_length=255, blank=True, null=True)
    lastnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    firstnamephonetic = models.CharField(max_length=255, blank=True, null=True)
    middlename = models.CharField(max_length=255, blank=True, null=True)
    alternatename = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_user'
        unique_together = (('mnethostid', 'username'),)


class McUserDevices(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    appid = models.CharField(max_length=128)
    name = models.CharField(max_length=32)
    model = models.CharField(max_length=32)
    platform = models.CharField(max_length=32)
    version = models.CharField(max_length=32)
    pushid = models.CharField(max_length=255)
    uuid = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_user_devices'
        unique_together = (('pushid', 'userid'),)


class McUserEnrolments(models.Model):
    id = models.BigAutoField(primary_key=True)
    status = models.BigIntegerField()
    enrolid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timestart = models.BigIntegerField()
    timeend = models.BigIntegerField()
    modifierid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_user_enrolments'
        unique_together = (('enrolid', 'userid'),)


class McUserInfoCategory(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    sortorder = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_user_info_category'


class McUserInfoData(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    fieldid = models.BigIntegerField()
    data = models.TextField()
    dataformat = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_user_info_data'
        unique_together = (('userid', 'fieldid'),)


class McUserInfoField(models.Model):
    id = models.BigAutoField(primary_key=True)
    shortname = models.CharField(max_length=255)
    name = models.TextField()
    datatype = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.IntegerField()
    categoryid = models.BigIntegerField()
    sortorder = models.BigIntegerField()
    required = models.IntegerField()
    locked = models.IntegerField()
    visible = models.SmallIntegerField()
    forceunique = models.IntegerField()
    signup = models.IntegerField()
    defaultdata = models.TextField(blank=True, null=True)
    defaultdataformat = models.IntegerField()
    param1 = models.TextField(blank=True, null=True)
    param2 = models.TextField(blank=True, null=True)
    param3 = models.TextField(blank=True, null=True)
    param4 = models.TextField(blank=True, null=True)
    param5 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_user_info_field'


class McUserLastaccess(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    courseid = models.BigIntegerField()
    timeaccess = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_user_lastaccess'
        unique_together = (('userid', 'courseid'),)


class McUserPasswordHistory(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    hash = models.CharField(max_length=255)
    timecreated = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_user_password_history'


class McUserPasswordResets(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    timerequested = models.BigIntegerField()
    timererequested = models.BigIntegerField()
    token = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'mc_user_password_resets'


class McUserPreferences(models.Model):
    id = models.BigAutoField(primary_key=True)
    userid = models.BigIntegerField()
    name = models.CharField(max_length=255)
    value = models.CharField(max_length=1333)

    class Meta:
        managed = False
        db_table = 'mc_user_preferences'
        unique_together = (('userid', 'name'),)


class McUserPrivateKey(models.Model):
    id = models.BigAutoField(primary_key=True)
    script = models.CharField(max_length=128)
    value = models.CharField(max_length=128)
    userid = models.BigIntegerField()
    instance = models.BigIntegerField(blank=True, null=True)
    iprestriction = models.CharField(max_length=255, blank=True, null=True)
    validuntil = models.BigIntegerField(blank=True, null=True)
    timecreated = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_user_private_key'


class McWebdavLocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    token = models.CharField(unique=True, max_length=255)
    path = models.CharField(max_length=255)
    expiry = models.BigIntegerField()
    userid = models.BigIntegerField()
    recursive = models.IntegerField()
    exclusivelock = models.IntegerField()
    created = models.BigIntegerField()
    modified = models.BigIntegerField()
    owner = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_webdav_locks'


class McWiki(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    firstpagetitle = models.CharField(max_length=255)
    wikimode = models.CharField(max_length=20)
    defaultformat = models.CharField(max_length=20)
    forceformat = models.IntegerField()
    editbegin = models.BigIntegerField()
    editend = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_wiki'


class McWikiLinks(models.Model):
    id = models.BigAutoField(primary_key=True)
    subwikiid = models.BigIntegerField()
    frompageid = models.BigIntegerField()
    topageid = models.BigIntegerField()
    tomissingpage = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_wiki_links'


class McWikiLocks(models.Model):
    id = models.BigAutoField(primary_key=True)
    pageid = models.BigIntegerField()
    sectionname = models.CharField(max_length=255, blank=True, null=True)
    userid = models.BigIntegerField()
    lockedat = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_wiki_locks'


class McWikiPages(models.Model):
    id = models.BigAutoField(primary_key=True)
    subwikiid = models.BigIntegerField()
    title = models.CharField(max_length=255)
    cachedcontent = models.TextField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    timerendered = models.BigIntegerField()
    userid = models.BigIntegerField()
    pageviews = models.BigIntegerField()
    readonly = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_wiki_pages'
        unique_together = (('subwikiid', 'title', 'userid'),)


class McWikiSubwikis(models.Model):
    id = models.BigAutoField(primary_key=True)
    wikiid = models.BigIntegerField()
    groupid = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_wiki_subwikis'
        unique_together = (('wikiid', 'groupid', 'userid'),)


class McWikiSynonyms(models.Model):
    id = models.BigAutoField(primary_key=True)
    subwikiid = models.BigIntegerField()
    pageid = models.BigIntegerField()
    pagesynonym = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'mc_wiki_synonyms'
        unique_together = (('pageid', 'pagesynonym'),)


class McWikiVersions(models.Model):
    id = models.BigAutoField(primary_key=True)
    pageid = models.BigIntegerField()
    content = models.TextField()
    contentformat = models.CharField(max_length=20)
    version = models.IntegerField()
    timecreated = models.BigIntegerField()
    userid = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'mc_wiki_versions'


class McWorkshop(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    intro = models.TextField(blank=True, null=True)
    introformat = models.SmallIntegerField()
    instructauthors = models.TextField(blank=True, null=True)
    instructauthorsformat = models.SmallIntegerField()
    instructreviewers = models.TextField(blank=True, null=True)
    instructreviewersformat = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    phase = models.SmallIntegerField(blank=True, null=True)
    useexamples = models.IntegerField(blank=True, null=True)
    usepeerassessment = models.IntegerField(blank=True, null=True)
    useselfassessment = models.IntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    strategy = models.CharField(max_length=30)
    evaluation = models.CharField(max_length=30)
    gradedecimals = models.SmallIntegerField(blank=True, null=True)
    nattachments = models.SmallIntegerField(blank=True, null=True)
    latesubmissions = models.IntegerField(blank=True, null=True)
    maxbytes = models.BigIntegerField(blank=True, null=True)
    examplesmode = models.SmallIntegerField(blank=True, null=True)
    submissionstart = models.BigIntegerField(blank=True, null=True)
    submissionend = models.BigIntegerField(blank=True, null=True)
    assessmentstart = models.BigIntegerField(blank=True, null=True)
    assessmentend = models.BigIntegerField(blank=True, null=True)
    phaseswitchassessment = models.IntegerField()
    conclusion = models.TextField(blank=True, null=True)
    conclusionformat = models.SmallIntegerField()
    overallfeedbackmode = models.SmallIntegerField(blank=True, null=True)
    overallfeedbackfiles = models.SmallIntegerField(blank=True, null=True)
    overallfeedbackmaxbytes = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop'


class McWorkshopAggregations(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    userid = models.BigIntegerField()
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    timegraded = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_aggregations'
        unique_together = (('workshopid', 'userid'),)


class McWorkshopAssessments(models.Model):
    id = models.BigAutoField(primary_key=True)
    submissionid = models.BigIntegerField()
    reviewerid = models.BigIntegerField()
    weight = models.BigIntegerField()
    timecreated = models.BigIntegerField(blank=True, null=True)
    timemodified = models.BigIntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggrade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggradeover = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradinggradeoverby = models.BigIntegerField(blank=True, null=True)
    feedbackauthor = models.TextField(blank=True, null=True)
    feedbackauthorformat = models.SmallIntegerField(blank=True, null=True)
    feedbackauthorattachment = models.SmallIntegerField(blank=True, null=True)
    feedbackreviewer = models.TextField(blank=True, null=True)
    feedbackreviewerformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_assessments'


class McWorkshopAssessmentsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    submissionid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timegraded = models.BigIntegerField()
    timeagreed = models.BigIntegerField()
    grade = models.FloatField()
    gradinggrade = models.SmallIntegerField()
    teachergraded = models.SmallIntegerField()
    mailed = models.SmallIntegerField()
    resubmission = models.SmallIntegerField()
    donotuse = models.SmallIntegerField()
    generalcomment = models.TextField(blank=True, null=True)
    teachercomment = models.TextField(blank=True, null=True)
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_assessments_old'


class McWorkshopCommentsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    assessmentid = models.BigIntegerField()
    userid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    mailed = models.IntegerField()
    comments = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_comments_old'


class McWorkshopElementsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.SmallIntegerField()
    description = models.TextField()
    scale = models.SmallIntegerField()
    maxscore = models.SmallIntegerField()
    weight = models.SmallIntegerField()
    stddev = models.FloatField()
    totalassessments = models.BigIntegerField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_elements_old'


class McWorkshopGrades(models.Model):
    id = models.BigAutoField(primary_key=True)
    assessmentid = models.BigIntegerField()
    strategy = models.CharField(max_length=30)
    dimensionid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    peercomment = models.TextField(blank=True, null=True)
    peercommentformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_grades'
        unique_together = (('assessmentid', 'strategy', 'dimensionid'),)


class McWorkshopGradesOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    assessmentid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    feedback = models.TextField()
    grade = models.SmallIntegerField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_grades_old'


class McWorkshopOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    course = models.BigIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    wtype = models.SmallIntegerField()
    nelements = models.SmallIntegerField()
    nattachments = models.SmallIntegerField()
    phase = models.IntegerField()
    format = models.IntegerField()
    gradingstrategy = models.IntegerField()
    resubmit = models.IntegerField()
    agreeassessments = models.IntegerField()
    hidegrades = models.IntegerField()
    anonymous = models.IntegerField()
    includeself = models.IntegerField()
    maxbytes = models.BigIntegerField()
    submissionstart = models.BigIntegerField()
    assessmentstart = models.BigIntegerField()
    submissionend = models.BigIntegerField()
    assessmentend = models.BigIntegerField()
    releasegrades = models.BigIntegerField()
    grade = models.SmallIntegerField()
    gradinggrade = models.SmallIntegerField()
    ntassessments = models.SmallIntegerField()
    assessmentcomps = models.SmallIntegerField()
    nsassessments = models.SmallIntegerField()
    overallocation = models.SmallIntegerField()
    timemodified = models.BigIntegerField()
    teacherweight = models.SmallIntegerField()
    showleaguetable = models.SmallIntegerField()
    usepassword = models.SmallIntegerField()
    password = models.CharField(max_length=32)
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_old'


class McWorkshopRubricsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    rubricno = models.SmallIntegerField()
    description = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_rubrics_old'


class McWorkshopStockcommentsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    elementno = models.BigIntegerField()
    comments = models.TextField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_stockcomments_old'


class McWorkshopSubmissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    example = models.IntegerField(blank=True, null=True)
    authorid = models.BigIntegerField()
    timecreated = models.BigIntegerField()
    timemodified = models.BigIntegerField()
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
    contentformat = models.SmallIntegerField()
    contenttrust = models.SmallIntegerField()
    attachment = models.IntegerField(blank=True, null=True)
    grade = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradeover = models.DecimalField(max_digits=10, decimal_places=5, blank=True, null=True)
    gradeoverby = models.BigIntegerField(blank=True, null=True)
    feedbackauthor = models.TextField(blank=True, null=True)
    feedbackauthorformat = models.SmallIntegerField(blank=True, null=True)
    timegraded = models.BigIntegerField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    late = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'mc_workshop_submissions'


class McWorkshopSubmissionsOld(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    userid = models.BigIntegerField()
    title = models.CharField(max_length=100)
    timecreated = models.BigIntegerField()
    mailed = models.IntegerField()
    description = models.TextField()
    gradinggrade = models.SmallIntegerField()
    finalgrade = models.SmallIntegerField()
    late = models.SmallIntegerField()
    nassessments = models.BigIntegerField()
    newplugin = models.CharField(max_length=28, blank=True, null=True)
    newid = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshop_submissions_old'


class McWorkshopallocationScheduled(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    enabled = models.IntegerField()
    submissionend = models.BigIntegerField()
    timeallocated = models.BigIntegerField(blank=True, null=True)
    settings = models.TextField(blank=True, null=True)
    resultstatus = models.BigIntegerField(blank=True, null=True)
    resultmessage = models.CharField(max_length=1333, blank=True, null=True)
    resultlog = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopallocation_scheduled'


class McWorkshopevalBestSettings(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    comparison = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopeval_best_settings'


class McWorkshopformAccumulative(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)
    grade = models.BigIntegerField()
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_accumulative'


class McWorkshopformComments(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_comments'


class McWorkshopformNumerrors(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)
    descriptiontrust = models.BigIntegerField(blank=True, null=True)
    grade0 = models.CharField(max_length=50, blank=True, null=True)
    grade1 = models.CharField(max_length=50, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_numerrors'


class McWorkshopformNumerrorsMap(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    nonegative = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_numerrors_map'
        unique_together = (('workshopid', 'nonegative'),)


class McWorkshopformRubric(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField()
    sort = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    descriptionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_rubric'


class McWorkshopformRubricConfig(models.Model):
    id = models.BigAutoField(primary_key=True)
    workshopid = models.BigIntegerField(unique=True)
    layout = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_rubric_config'


class McWorkshopformRubricLevels(models.Model):
    id = models.BigAutoField(primary_key=True)
    dimensionid = models.BigIntegerField()
    grade = models.DecimalField(max_digits=10, decimal_places=5)
    definition = models.TextField(blank=True, null=True)
    definitionformat = models.SmallIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'mc_workshopform_rubric_levels'
