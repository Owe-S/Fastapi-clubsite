from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    Date,
    DECIMAL,
    Float,
    SmallInteger,
    Text,
    CHAR,
    ForeignKey,
)
from sqlalchemy.orm import relationship
from database import Base

class SiteUser(Base):
    __tablename__ = "Siteusers"
    userID      = Column(Integer, primary_key=True)
    memberID    = Column(String(20))
    gender      = Column(CHAR(1), nullable=False)
    boolPrivate = Column(Boolean, nullable=False)
    userName    = Column(String(50))
    lastName    = Column(String(30))
    firstName   = Column(String(30))
    hcp         = Column(Integer)
    email       = Column(String(50))
    pwdHash     = Column(String(40))
    telephone   = Column(String(20))
    regDate     = Column(DateTime)

class NewsArticle(Base):
    __tablename__ = "News_Articles"
    articleID       = Column(Integer, primary_key=True)
    depID           = Column(Integer, nullable=False)
    boolPubl        = Column(Boolean, nullable=False)
    boolShow        = Column(Boolean, nullable=False)
    boolPri         = Column(Boolean, nullable=False)
    template        = Column(SmallInteger)
    validfrom       = Column(DateTime, nullable=False)
    validto         = Column(DateTime, nullable=False)
    author          = Column(String(100))
    heading         = Column(String(100), nullable=False)
    urlTitle        = Column(String(200), nullable=False)
    indexImageID    = Column(Integer)
    indexImage      = Column(String(100))
    indexImagePath  = Column(String(200))
    indeximg_descr  = Column(String(500))
    templateImageID = Column(Integer)
    templateImage   = Column(String(200))
    templimg_descr  = Column(String(500))
    ingress         = Column(String(1000))
    newscontent     = Column(Text)
    pagedescription = Column(String(500))
    useFBcomments   = Column(Boolean)
    date_published  = Column(DateTime)
    date_created    = Column(DateTime, nullable=False)
    created_by      = Column(String(100))
    date_modified   = Column(DateTime)
    modified_by     = Column(String(100))
    amtReceivers    = Column(Integer)
    videoUrl        = Column(String(200))
    boolInfoscreen  = Column(Boolean)
    boolBoxed       = Column(Boolean)
    boolRss         = Column(Boolean)
    boolToFacebook  = Column(Boolean)

class Activities(Base):
    __tablename__ = "Activities"
    __table_args__ = {"extend_existing": True}

    activityID            = Column(Integer, primary_key=True)
    listID                = Column(Integer, nullable=False)
    boolShow              = Column(Boolean, nullable=False)
    activityName          = Column(String(100), nullable=False)
    actAlias              = Column(String(100))
    location              = Column(String(200))
    maxParticipants       = Column(SmallInteger)
    boolWaitlist          = Column(Boolean)
    partReserved          = Column(SmallInteger)
    date_start            = Column(DateTime)
    time_from             = Column(String(4))
    time_to               = Column(String(4))
    boolOnlinePay         = Column(Boolean, nullable=False)
    boolOnlineSignup      = Column(Boolean, nullable=False)
    formID                = Column(Integer)
    priceGroupID          = Column(Integer)
    signup_from           = Column(DateTime)
    signup_to             = Column(DateTime)
    actDescription        = Column(String(5000))
    boolSignupToMail      = Column(Boolean)
    signupMailTo          = Column(String(50))
    date_created          = Column(DateTime, nullable=False)
    created_by            = Column(String(100), nullable=False)
    date_modified         = Column(DateTime)
    modified_by           = Column(String(100))
    boolVTG               = Column(Boolean)
    boolVTGforward        = Column(Boolean)
    payAccount            = Column(Integer)
    boolMemberRequired    = Column(Boolean)
    actLocation           = Column(String(200))
    field_borrowEquipment = Column(Boolean)

class ActivitiesDateTime(Base):
    __tablename__ = "Activities_DateTime"
    activityID = Column(Integer, primary_key=True)
    actDate    = Column(Date, primary_key=True)
    time_from  = Column(String(5))
    time_to    = Column(String(5))
    actDay     = Column(SmallInteger)

# --- Image models ---
class Images(Base):
    __tablename__ = "Images"
    imageID       = Column(Integer, primary_key=True, index=True)
    depID         = Column(Integer, nullable=False)
    categoryID    = Column(Integer, ForeignKey("Images_Categories.categoryID"), nullable=False)
    imgWidth      = Column(Integer)
    imgHeight     = Column(Integer)
    imagename     = Column(String(100), nullable=False)
    imagefile     = Column(String(100))
    imgDescription= Column(String(100))
    credits       = Column(String(100))
    sizecat       = Column(Integer)
    boolBoxed     = Column(Boolean)
    date_created  = Column(DateTime)
    created_by    = Column(String(100))

    category = relationship("Images_Categories", back_populates="images")

class Images_Categories(Base):
    __tablename__ = "Images_Categories"
    categoryID = Column(Integer, primary_key=True, index=True)
    depID      = Column(Integer, nullable=False)
    category   = Column(String(100), nullable=False)

    images = relationship("Images", back_populates="category")

class Courses(Base):
    __tablename__ = "Courses"
    courseID   = Column(Integer, primary_key=True, index=True)
    coursename = Column(String(100), nullable=False)
    urlTitle   = Column(String(100))
    holes      = Column(SmallInteger, nullable=False)
    sortnum    = Column(SmallInteger, nullable=False)
    boolShow   = Column(Boolean, nullable=False)
    boolSlope  = Column(Boolean)

    guide_images   = relationship("Course_Guide_Images",   back_populates="course")
    guide_sponsors = relationship("Course_Guide_Sponsors", back_populates="course")


class CourseGuideImages(Base):
    __tablename__ = "Course_Guide_Images"
    imageID        = Column(Integer, primary_key=True, index=True)
    hole           = Column(SmallInteger, nullable=False)
    courseID       = Column(Integer, ForeignKey("Courses.courseID"), nullable=False)
    imagefile      = Column(String(100))
    imgDescription = Column(String(100))
    sortnum        = Column(SmallInteger)

    course = relationship("Courses", back_populates="guide_images")


class CourseGuideSponsors(Base):
    __tablename__ = "Course_Guide_Sponsors"
    sponsorID = Column(Integer, primary_key=True, index=True)
    courseID  = Column(Integer, ForeignKey("Courses.courseID"), nullable=True)
    hole      = Column(SmallInteger, nullable=False)

    course = relationship("Courses", back_populates="guide_sponsors")


class CourseGuideHole(Base):
    __tablename__ = "Course_Guide_Hole"
    holeID   = Column(Integer, primary_key=True, index=True)
    videourl = Column(String(500))


class CoursesHio(Base):
    __tablename__ = "Courses_Hio"
    hioID = Column(Integer, primary_key=True, index=True)

# --- AdminAreas ---
class AdminAreas(Base):
    __tablename__ = "Admin_Areas"
    areaID = Column(Integer, primary_key=True, index=True)
    area   = Column(String(30), nullable=False)

# --- AdminUserPwdtemp ---
class AdminUserPwdtemp(Base):
    __tablename__ = "Admin_User_PwdTemp"
    userID    = Column(String(50), primary_key=True, index=True)
    pwdKey    = Column(String(32), nullable=False)
    pwdNumber = Column(Integer,   nullable=False)
    timestamp = Column(DateTime,  nullable=False)

# -- AUTO GENERATED MODELS START
class ActivitiesParticipants(Base):
    __tablename__ = "Activities_Participants"
    participantID = Column(Integer, primary_key=True)
    activityID = Column(Integer)
    boolSuConfirmed = Column(Boolean)
    orderID = Column(Integer, nullable=True)
    price = Column(DECIMAL, nullable=True)
    pricecat = Column(String(50), nullable=True)
    onWaitlist = Column(Boolean, nullable=True)
    parentname = Column(String(80), nullable=True)
    fname = Column(String(50))
    sname = Column(String(50))
    email = Column(String(100), nullable=True)
    memberID = Column(String(30), nullable=True)
    bornyear = Column(String(10), nullable=True)
    address = Column(String(100), nullable=True)
    pcodecity = Column(String(100), nullable=True)
    postcode = Column(String(20), nullable=True)
    city = Column(String(50), nullable=True)
    telephone = Column(String(50), nullable=True)
    hcp = Column(String(10), nullable=True)
    homeClub = Column(String(50), nullable=True)
    comments = Column(String(500), nullable=True)
    extraInfo = Column(String(500), nullable=True)
    date_signup = Column(DateTime, nullable=True)
    signupKey = Column(String(32), nullable=True)
    vtgMembership = Column(Boolean, nullable=True)
    memberByVtg = Column(Boolean, nullable=True)
    parentemail = Column(String(80), nullable=True)
    parentphone = Column(String(30), nullable=True)
    boolDeleted = Column(Boolean, nullable=True)

class ActivitiesPricegroupPrices(Base):
    __tablename__ = "Activities_PriceGroup_Prices"
    priceCatID = Column(Integer, primary_key=True)
    groupID = Column(Integer)
    pricecatname = Column(String(50))
    price = Column(DECIMAL)

class ActivitiesPricegroups(Base):
    __tablename__ = "Activities_PriceGroups"
    groupID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    actType = Column(String(20))
    priceGroup = Column(String(50))
    boolActive = Column(Boolean, nullable=True)

class ActivitiesPrices(Base):
    __tablename__ = "Activities_Prices"
    priceID = Column(Integer, primary_key=True)
    activityID = Column(Integer, nullable=True)
    tournID = Column(Integer, nullable=True)
    pricecat = Column(String(50))
    price = Column(DECIMAL)

class AdminUsers(Base):
    __tablename__ = "Admin_Users"
    userID = Column(Integer, primary_key=True)
    boolSupervisor = Column(Boolean)
    adminName = Column(String(100))
    adminEmail = Column(String(100))
    pwd_hash = Column(String(32))
    pwd_temp = Column(String(30), nullable=True)
    date_created = Column(DateTime)
    lastLog = Column(DateTime, nullable=True)
    cKey = Column(String(32), nullable=True)

class AdminUsersAreas(Base):
    __tablename__ = "Admin_Users_Areas"
    areaID = Column(Integer, primary_key=True)
    userID = Column(Integer)

class AdminUsersDepartments(Base):
    __tablename__ = "Admin_Users_Departments"
    userID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    preferred = Column(Boolean)

class Ads(Base):
    __tablename__ = "Ads"
    adID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean)
    catID = Column(Integer, nullable=True)
    contact = Column(String(80), nullable=True)
    email = Column(String(80), nullable=True)
    phone = Column(String(30), nullable=True)
    price = Column(String(100), nullable=True)
    date_created = Column(DateTime, nullable=True)

class AdsCategories(Base):
    __tablename__ = "Ads_Categories"
    catID = Column(Integer, primary_key=True)
    category = Column(String(30), nullable=True)

class Attachments(Base):
    __tablename__ = "Attachments"
    attachmentID = Column(Integer, primary_key=True)
    documentID = Column(Integer)
    pageID = Column(Integer, nullable=True)
    articleID = Column(Integer, nullable=True)
    tournID = Column(Integer, nullable=True)
    activityID = Column(Integer, nullable=True)
    safeField = Column(Integer, nullable=True)

class Blog(Base):
    __tablename__ = "Blog"
    blogID = Column(Integer, primary_key=True)
    bloggerID = Column(Integer, nullable=True)
    boolShow = Column(Boolean)
    typeComments = Column(String(2), nullable=True)
    pagedescription = Column(String(500), nullable=True)
    template = Column(SmallInteger, nullable=True)
    indexImageID = Column(Integer, nullable=True)
    indexImage = Column(String(100), nullable=True)
    indexImagePath = Column(String(200), nullable=True)
    indeximg_descr = Column(String(500), nullable=True)
    templateImageID = Column(Integer, nullable=True)
    templateImage = Column(String(200), nullable=True)
    templimg_descr = Column(String(500), nullable=True)
    validfrom = Column(DateTime)
    heading = Column(String(250))
    urlTitle = Column(String(200))
    blogContent = Column(String, nullable=True)
    boolSendNotice = Column(Boolean, nullable=True)
    noticeToEmail = Column(String(100), nullable=True)
    date_created = Column(DateTime)
    created_by = Column(String(100))
    videoUrl = Column(String(200), nullable=True)

class BlogComments(Base):
    __tablename__ = "Blog_Comments"
    commentID = Column(Integer, primary_key=True)
    blogID = Column(Integer)
    comment = Column(String(500))
    boolShow = Column(Boolean)
    poster = Column(String(100))
    poster_email = Column(String(100), nullable=True)
    date_created = Column(DateTime)
    admin_comment = Column(String(500), nullable=True)
    bloggerID = Column(Integer, nullable=True)
    date_reply = Column(DateTime, nullable=True)

class BlogImages(Base):
    __tablename__ = "Blog_Images"
    imageID = Column(Integer, primary_key=True)
    bloggerID = Column(Integer)
    imgWidth = Column(String(4), nullable=True)
    imgHeight = Column(String(4), nullable=True)
    imagefile = Column(String(100))
    imgDescription = Column(String(200), nullable=True)
    sizecat = Column(SmallInteger, nullable=True)
    date_created = Column(DateTime, nullable=True)

class Bloggers(Base):
    __tablename__ = "Bloggers"
    bloggerID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean, nullable=True)
    bloggerName = Column(String(50), nullable=True)
    bloggerAlias = Column(String(50), nullable=True)
    bloggerLogin = Column(String(50), nullable=True)
    bloggerEmail = Column(String(100), nullable=True)
    pwdHash = Column(String(32), nullable=True)
    ckey = Column(String(32), nullable=True)
    date_created = Column(DateTime, nullable=True)
    created_by = Column(String(100), nullable=True)

class Calendar(Base):
    __tablename__ = "Calendar"
    calID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    descr = Column(String(200))
    tournID = Column(Integer, nullable=True)
    activityID = Column(Integer, nullable=True)
    calDate = Column(DateTime)
    timeFrom = Column(String(4))
    timeTo = Column(String(4))
    details = Column(String(300), nullable=True)

class Cart(Base):
    __tablename__ = "Cart"
    cartRowID = Column(Integer, primary_key=True)
    cartID = Column(String(50))
    noProd = Column(Boolean)
    productID = Column(Integer, nullable=True)
    prodVarID = Column(Integer, nullable=True)
    activityID = Column(Integer, nullable=True)
    tournID = Column(Integer, nullable=True)
    feedbackID = Column(Integer, nullable=True)
    senderID = Column(Integer, nullable=True)
    participantID = Column(Integer, nullable=True)
    variant = Column(String(200), nullable=True)
    textVariant = Column(String(200), nullable=True)
    totPrice = Column(DECIMAL)
    quantity = Column(Integer)
    totalValue = Column(DECIMAL, nullable=True)
    dateAdded = Column(DateTime)
    ip = Column(String(20), nullable=True)
    memberRecID = Column(Integer, nullable=True)
    payAccount = Column(Integer, nullable=True)

class Clubchamps(Base):
    __tablename__ = "ClubChamps"
    championID = Column(Integer, primary_key=True)
    ch_year = Column(String(4), nullable=True)
    categoryID = Column(Integer, nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    rounds = Column(String(2), nullable=True)
    score = Column(String(20), nullable=True)
    imagepath = Column(String(250), nullable=True)
    tee = Column(String(20), nullable=True)
    url_res = Column(String(300), nullable=True)

class ClubchampsCategories(Base):
    __tablename__ = "ClubChamps_Categories"
    categoryID = Column(Integer, primary_key=True)
    category = Column(String(100), nullable=True)
    sortnum = Column(SmallInteger, nullable=True)
    tee = Column(String(20), nullable=True)

class Contacts(Base):
    __tablename__ = "Contacts"
    contactID = Column(Integer, primary_key=True)
    listID = Column(Integer)
    profileID = Column(Integer)
    sortnum = Column(SmallInteger)
    contactTitle = Column(String(50), nullable=True)

class ContactsList(Base):
    __tablename__ = "Contacts_List"
    listID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    listname = Column(String(50))
    listtype = Column(String(20), nullable=True)
    sortnum = Column(SmallInteger)
    boolShow = Column(Boolean)
    useDescription = Column(Boolean, nullable=True)
    useIcons = Column(Boolean, nullable=True)

class CoursesPar(Base):
    __tablename__ = "Courses_Par"
    courseID = Column(Integer, primary_key=True)
    p1 = Column(SmallInteger, nullable=True)
    p2 = Column(SmallInteger, nullable=True)
    p3 = Column(SmallInteger, nullable=True)
    p4 = Column(SmallInteger, nullable=True)
    p5 = Column(SmallInteger, nullable=True)
    p6 = Column(SmallInteger, nullable=True)
    p7 = Column(SmallInteger, nullable=True)
    p8 = Column(SmallInteger, nullable=True)
    p9 = Column(SmallInteger, nullable=True)
    p10 = Column(SmallInteger, nullable=True)
    p11 = Column(SmallInteger, nullable=True)
    p12 = Column(SmallInteger, nullable=True)
    p13 = Column(SmallInteger, nullable=True)
    p14 = Column(SmallInteger, nullable=True)
    p15 = Column(SmallInteger, nullable=True)
    p16 = Column(SmallInteger, nullable=True)
    p17 = Column(SmallInteger, nullable=True)
    p18 = Column(SmallInteger, nullable=True)
    pfront = Column(SmallInteger, nullable=True)
    pback = Column(SmallInteger, nullable=True)
    par = Column(SmallInteger, nullable=True)
    i1 = Column(SmallInteger, nullable=True)
    i2 = Column(SmallInteger, nullable=True)
    i3 = Column(SmallInteger, nullable=True)
    i4 = Column(SmallInteger, nullable=True)
    i5 = Column(SmallInteger, nullable=True)
    i6 = Column(SmallInteger, nullable=True)
    i7 = Column(SmallInteger, nullable=True)
    i8 = Column(SmallInteger, nullable=True)
    i9 = Column(SmallInteger, nullable=True)
    i10 = Column(SmallInteger, nullable=True)
    i11 = Column(SmallInteger, nullable=True)
    i12 = Column(SmallInteger, nullable=True)
    i13 = Column(SmallInteger, nullable=True)
    i14 = Column(SmallInteger, nullable=True)
    i15 = Column(SmallInteger, nullable=True)
    i16 = Column(SmallInteger, nullable=True)
    i17 = Column(SmallInteger, nullable=True)
    i18 = Column(SmallInteger, nullable=True)
    n1 = Column(String(30), nullable=True)
    n2 = Column(String(30), nullable=True)
    n3 = Column(String(30), nullable=True)
    n4 = Column(String(30), nullable=True)
    n5 = Column(String(30), nullable=True)
    n6 = Column(String(30), nullable=True)
    n7 = Column(String(30), nullable=True)
    n8 = Column(String(30), nullable=True)
    n9 = Column(String(30), nullable=True)
    n10 = Column(String(30), nullable=True)
    n11 = Column(String(30), nullable=True)
    n12 = Column(String(30), nullable=True)
    n13 = Column(String(30), nullable=True)
    n14 = Column(String(30), nullable=True)
    n15 = Column(String(30), nullable=True)
    n16 = Column(String(30), nullable=True)
    n17 = Column(String(30), nullable=True)
    n18 = Column(String(30), nullable=True)

class CoursesTees(Base):
    __tablename__ = "Courses_Tees"
    teeID = Column(Integer, primary_key=True)
    courseID = Column(Integer)
    sortnum = Column(SmallInteger)
    teename = Column(String(20))
    cr_m = Column(Float, nullable=True)
    cr_f = Column(Float, nullable=True)
    slope_m = Column(SmallInteger, nullable=True)
    slope_f = Column(SmallInteger, nullable=True)
    l1 = Column(String, nullable=True)
    l2 = Column(String, nullable=True)
    l3 = Column(String, nullable=True)
    l4 = Column(String, nullable=True)
    l5 = Column(String, nullable=True)
    l6 = Column(String, nullable=True)
    l7 = Column(String, nullable=True)
    l8 = Column(String, nullable=True)
    l9 = Column(String, nullable=True)
    l10 = Column(String, nullable=True)
    l11 = Column(String, nullable=True)
    l12 = Column(String, nullable=True)
    l13 = Column(String, nullable=True)
    l14 = Column(String, nullable=True)
    l15 = Column(String, nullable=True)
    l16 = Column(String, nullable=True)
    l17 = Column(String, nullable=True)
    l18 = Column(String, nullable=True)
    lf9 = Column(String, nullable=True)
    lb9 = Column(String, nullable=True)
    ltotal = Column(String, nullable=True)

class Departments(Base):
    __tablename__ = "Departments"
    depID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean)
    boolMainDep = Column(Boolean)
    department = Column(String(100))
    urlAlias = Column(String(100))
    slogan = Column(String(300), nullable=True)
    megasort = Column(SmallInteger, nullable=True)
    date_created = Column(DateTime)
    boolRequired = Column(Boolean, nullable=True)
    boolMemberArea = Column(Boolean, nullable=True)
    boolModuleDirect = Column(Boolean, nullable=True)

class Documents(Base):
    __tablename__ = "Documents"
    documentID = Column(Integer, primary_key=True)
    oldDokID = Column(Integer, nullable=True)
    depID = Column(Integer)
    boolShow = Column(Boolean)
    categoryID = Column(Integer)
    docname = Column(String(100))
    docdescription = Column(String(300), nullable=True)
    docformat = Column(String(5))
    docfile = Column(String(100))
    size = Column(String(10))
    date_created = Column(DateTime)
    date_updated = Column(DateTime, nullable=True)
    created_by = Column(String(100))

class DocumentsCategories(Base):
    __tablename__ = "Documents_Categories"
    categoryID = Column(Integer, primary_key=True)
    parentID = Column(Integer, nullable=True)
    depID = Column(Integer)
    category = Column(String(100))
    start = Column(Boolean)

class DocumentsUserreg(Base):
    __tablename__ = "Documents_Userreg"
    documentID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean)
    categoryID = Column(Integer, nullable=True)
    docname = Column(String(100))
    docdescription = Column(String(300), nullable=True)
    docformat = Column(String(5))
    docfile = Column(String(100))
    size = Column(String(10), nullable=True)
    date_created = Column(DateTime)
    date_updated = Column(DateTime, nullable=True)
    created_by = Column(String(100), nullable=True)

class DocumentsUserregCategories(Base):
    __tablename__ = "Documents_Userreg_Categories"
    categoryID = Column(Integer, primary_key=True)
    category = Column(String(100))

class EclecticCourses(Base):
    __tablename__ = "Eclectic_Courses"
    ecl_tournID = Column(Integer, primary_key=True)
    coursename = Column(String(50))
    p1 = Column(SmallInteger, nullable=True)
    p2 = Column(SmallInteger, nullable=True)
    p3 = Column(SmallInteger, nullable=True)
    p4 = Column(SmallInteger, nullable=True)
    p5 = Column(SmallInteger, nullable=True)
    p6 = Column(SmallInteger, nullable=True)
    p7 = Column(SmallInteger, nullable=True)
    p8 = Column(SmallInteger, nullable=True)
    p9 = Column(SmallInteger, nullable=True)
    p10 = Column(SmallInteger, nullable=True)
    p11 = Column(SmallInteger, nullable=True)
    p12 = Column(SmallInteger, nullable=True)
    p13 = Column(SmallInteger, nullable=True)
    p14 = Column(SmallInteger, nullable=True)
    p15 = Column(SmallInteger, nullable=True)
    p16 = Column(SmallInteger, nullable=True)
    p17 = Column(SmallInteger, nullable=True)
    p18 = Column(SmallInteger, nullable=True)
    pfront = Column(SmallInteger, nullable=True)
    pback = Column(SmallInteger, nullable=True)
    par = Column(SmallInteger, nullable=True)
    i1 = Column(SmallInteger, nullable=True)
    i2 = Column(SmallInteger, nullable=True)
    i3 = Column(SmallInteger, nullable=True)
    i4 = Column(SmallInteger, nullable=True)
    i5 = Column(SmallInteger, nullable=True)
    i6 = Column(SmallInteger, nullable=True)
    i7 = Column(SmallInteger, nullable=True)
    i8 = Column(SmallInteger, nullable=True)
    i9 = Column(SmallInteger, nullable=True)
    i10 = Column(SmallInteger, nullable=True)
    i11 = Column(SmallInteger, nullable=True)
    i12 = Column(SmallInteger, nullable=True)
    i13 = Column(SmallInteger, nullable=True)
    i14 = Column(SmallInteger, nullable=True)
    i15 = Column(SmallInteger, nullable=True)
    i16 = Column(SmallInteger, nullable=True)
    i17 = Column(SmallInteger, nullable=True)
    i18 = Column(SmallInteger, nullable=True)

class EclecticParticipants(Base):
    __tablename__ = "Eclectic_Participants"
    participantID = Column(Integer, primary_key=True)
    oldID = Column(Integer, nullable=True)
    ecl_TournID = Column(Integer, nullable=True)
    fname = Column(String(30), nullable=True)
    lname = Column(String(50), nullable=True)
    hcp = Column(String, nullable=True)

class EclecticScore(Base):
    __tablename__ = "Eclectic_Score"
    scoreID = Column(Integer, primary_key=True)
    ecl_tournID = Column(Integer)
    participantID = Column(Integer)
    hcp = Column(String, nullable=True)
    MS = Column(SmallInteger, nullable=True)
    scoreDate = Column(DateTime)
    sc1 = Column(String, nullable=True)
    sc2 = Column(String, nullable=True)
    sc3 = Column(String, nullable=True)
    sc4 = Column(String, nullable=True)
    sc5 = Column(String, nullable=True)
    sc6 = Column(String, nullable=True)
    sc7 = Column(String, nullable=True)
    sc8 = Column(String, nullable=True)
    sc9 = Column(String, nullable=True)
    sc10 = Column(String, nullable=True)
    sc11 = Column(String, nullable=True)
    sc12 = Column(String, nullable=True)
    sc13 = Column(String, nullable=True)
    sc14 = Column(String, nullable=True)
    sc15 = Column(String, nullable=True)
    sc16 = Column(String, nullable=True)
    sc17 = Column(String, nullable=True)
    sc18 = Column(String, nullable=True)
    sumScore = Column(String, nullable=True)
    sumAlb = Column(String, nullable=True)
    sumEag = Column(String, nullable=True)
    sumBir = Column(String, nullable=True)
    sumPar = Column(String, nullable=True)
    sumBog = Column(String, nullable=True)
    sumDbo = Column(String, nullable=True)
    sumOth = Column(String, nullable=True)

class EclecticScoreNet(Base):
    __tablename__ = "Eclectic_Score_Net"
    scoreID = Column(Integer, primary_key=True)
    ecl_tournID = Column(Integer)
    participantID = Column(Integer)
    sc1 = Column(String, nullable=True)
    sc2 = Column(String, nullable=True)
    sc3 = Column(String, nullable=True)
    sc4 = Column(String, nullable=True)
    sc5 = Column(String, nullable=True)
    sc6 = Column(String, nullable=True)
    sc7 = Column(String, nullable=True)
    sc8 = Column(String, nullable=True)
    sc9 = Column(String, nullable=True)
    sc10 = Column(String, nullable=True)
    sc11 = Column(String, nullable=True)
    sc12 = Column(String, nullable=True)
    sc13 = Column(String, nullable=True)
    sc14 = Column(String, nullable=True)
    sc15 = Column(String, nullable=True)
    sc16 = Column(String, nullable=True)
    sc17 = Column(String, nullable=True)
    sc18 = Column(String, nullable=True)
    sumScore = Column(String, nullable=True)

class EclecticScoreStbl(Base):
    __tablename__ = "Eclectic_Score_Stbl"
    scoreID = Column(Integer, primary_key=True)
    participantID = Column(Integer)
    ecl_tournID = Column(Integer)
    sc1 = Column(String, nullable=True)
    sc2 = Column(String, nullable=True)
    sc3 = Column(String, nullable=True)
    sc4 = Column(String, nullable=True)
    sc5 = Column(String, nullable=True)
    sc6 = Column(String, nullable=True)
    sc7 = Column(String, nullable=True)
    sc8 = Column(String, nullable=True)
    sc9 = Column(String, nullable=True)
    sc10 = Column(String, nullable=True)
    sc11 = Column(String, nullable=True)
    sc12 = Column(String, nullable=True)
    sc13 = Column(String, nullable=True)
    sc14 = Column(String, nullable=True)
    sc15 = Column(String, nullable=True)
    sc16 = Column(String, nullable=True)
    sc17 = Column(String, nullable=True)
    sc18 = Column(String, nullable=True)
    sumScore = Column(String)

class EclecticTournaments(Base):
    __tablename__ = "Eclectic_Tournaments"
    ecl_tournID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    boolShow = Column(Boolean)
    holes = Column(String(5))
    tournName = Column(String(100))
    eclAlias = Column(String(100))
    tournInfo = Column(String(2000), nullable=True)
    tournType = Column(SmallInteger)
    rangType = Column(SmallInteger)
    sortnum = Column(SmallInteger, nullable=True)

class ElementsDateslider(Base):
    __tablename__ = "Elements_Dateslider"
    img_mon = Column(String(100), primary_key=True, nullable=True)
    img_tue = Column(String(100), nullable=True)
    img_wed = Column(String(100), nullable=True)
    img_thu = Column(String(100), nullable=True)
    img_fri = Column(String(100), nullable=True)
    img_sat = Column(String(100), nullable=True)
    img_sun = Column(String(100), nullable=True)
    useStaticContent = Column(Boolean, nullable=True)
    staticContent = Column(String, nullable=True)
    sliderbox_useicon = Column(Boolean, nullable=True)

class ElementsDatesliderDates(Base):
    __tablename__ = "Elements_Dateslider_Dates"
    img_date = Column(DateTime, primary_key=True, nullable=True)
    img_file = Column(String(100), nullable=True)

class ElementsDatesliderSlides(Base):
    __tablename__ = "Elements_Dateslider_Slides"
    slideID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean, nullable=True)
    align_vert = Column(String(30), nullable=True)
    align_hor = Column(String(30), nullable=True)
    lineBig = Column(String(80), nullable=True)
    lineSmall = Column(String(200), nullable=True)
    button_1_text = Column(String(30), nullable=True)
    button_1_url = Column(String(250), nullable=True)
    button_2_text = Column(String(30), nullable=True)
    button_2_url = Column(String(250), nullable=True)
    sortnum = Column(SmallInteger, nullable=True)
    button_3_text = Column(String(30), nullable=True)
    button_3_url = Column(String(250), nullable=True)
    button_1_url_ext = Column(Boolean, nullable=True)
    button_2_url_ext = Column(Boolean, nullable=True)
    button_3_url_ext = Column(Boolean, nullable=True)
    button_4_text = Column(String(30), nullable=True)
    button_4_url = Column(String(250), nullable=True)
    button_4_url_ext = Column(Boolean, nullable=True)

class ElementsFlexsliderElements(Base):
    __tablename__ = "Elements_Flexslider_Elements"
    elementID = Column(Integer, primary_key=True)
    sliderID = Column(Integer)
    boolShow = Column(Boolean, nullable=True)
    elName = Column(String(100))
    elImagefile = Column(String(50), nullable=True)
    elUrl = Column(String(100), nullable=True)
    elCaption = Column(String(200), nullable=True)
    sortnum = Column(SmallInteger)

class ElementsFlexsliderSliders(Base):
    __tablename__ = "Elements_Flexslider_Sliders"
    sliderID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean)
    slidername = Column(String(100))
    comments = Column(String(300), nullable=True)
    height = Column(String(3), nullable=True)
    boolFullwidth = Column(Boolean, nullable=True)
    boolTwothird = Column(Boolean, nullable=True)
    boolOnethird = Column(Boolean, nullable=True)
    date_created = Column(DateTime)
    created_by = Column(String(50), nullable=True)

class ElementsLayersliderLayers(Base):
    __tablename__ = "Elements_Layerslider_Layers"
    layerID = Column(Integer, primary_key=True)
    slideID = Column(Integer, nullable=True)
    pauseIn = Column(String(5), nullable=True)
    distTop = Column(String(10), nullable=True)
    distLeft = Column(String(10), nullable=True)
    animIn = Column(String(20), nullable=True)
    animOut = Column(String(20), nullable=True)
    textAlign = Column(String(10), nullable=True)
    lineBig = Column(String(100), nullable=True)
    lineSmall = Column(String(100), nullable=True)
    button_1_text = Column(String(30), nullable=True)
    button_1_url = Column(String(250), nullable=True)
    button_2_text = Column(String(30), nullable=True)
    button_2_url = Column(String(250), nullable=True)

class ElementsLayersliderSlides(Base):
    __tablename__ = "Elements_Layerslider_Slides"
    slideID = Column(Integer, primary_key=True)
    parentID = Column(Integer, nullable=True)
    sortnum = Column(SmallInteger)
    boolShow = Column(Boolean, nullable=True)
    slide_name = Column(String(50))
    slide_delay = Column(String(5))
    slide_transition = Column(String(5))
    bg_image = Column(String(100))

class Faq(Base):
    __tablename__ = "FAQ"
    qID = Column(Integer, primary_key=True)
    categoryID = Column(Integer, nullable=True)
    boolShow = Column(Boolean)
    question = Column(String(200))
    answer = Column(String(3000), nullable=True)
    sortnum = Column(SmallInteger)
    depID = Column(Integer, nullable=True)

class FaqCategories(Base):
    __tablename__ = "FAQ_Categories"
    categoryID = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=True)
    boolShow = Column(Boolean, nullable=True)
    sortnum = Column(SmallInteger, nullable=True)
    depID = Column(Integer, nullable=True)

class Feedbacks(Base):
    __tablename__ = "Feedbacks"
    feedbackID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    feedbackName = Column(String(100), nullable=True)
    activefrom = Column(DateTime, nullable=True)
    activeto = Column(DateTime, nullable=True)
    formID = Column(Integer, nullable=True)
    priceGroupID = Column(Integer, nullable=True)
    boolFormToMail = Column(Boolean, nullable=True)
    admMailTo = Column(String(80), nullable=True)
    boolOnlinePay = Column(Boolean, nullable=True)
    date_created = Column(DateTime)
    created_by = Column(String(100))

class FeedbacksIn(Base):
    __tablename__ = "Feedbacks_In"
    senderID = Column(Integer, primary_key=True)
    feedbackID = Column(Integer)
    boolSuConfirmed = Column(Boolean)
    orderID = Column(Integer, nullable=True)
    price = Column(DECIMAL, nullable=True)
    pricecat = Column(String(50), nullable=True)
    parentinfo = Column(String(80), nullable=True)
    fname = Column(String(50), nullable=True)
    lname = Column(String(100), nullable=True)
    fullname = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    memberID = Column(String(30), nullable=True)
    bornyear = Column(String(4), nullable=True)
    address = Column(String(100), nullable=True)
    pcodecity = Column(String(100), nullable=True)
    postcode = Column(String(20), nullable=True)
    city = Column(String(50), nullable=True)
    telephone = Column(String(50), nullable=True)
    hcp = Column(String(10), nullable=True)
    seldate = Column(Date, nullable=True)
    homeClub = Column(String(50), nullable=True)
    comments = Column(String(500), nullable=True)
    extraInfo = Column(String(500), nullable=True)
    date_created = Column(DateTime, nullable=True)

class Forms(Base):
    __tablename__ = "Forms"
    formID = Column(Integer, primary_key=True)
    depID = Column(Integer, nullable=True)
    formName = Column(String(50))
    formType = Column(String(50), nullable=True)
    formDescription = Column(String(500), nullable=True)
    mailReceiver = Column(String(100), nullable=True)
    date_created = Column(DateTime, nullable=True)
    date_updated = Column(DateTime, nullable=True)
    created_by = Column(String(100), nullable=True)

class FormsBymail(Base):
    __tablename__ = "Forms_Bymail"
    recID = Column(Integer, primary_key=True)
    formID = Column(Integer, nullable=True)
    formname = Column(String(100), nullable=True)
    maildate = Column(DateTime)
    tomail = Column(String(100), nullable=True)
    fromname = Column(String(100), nullable=True)
    fromemail = Column(String(100), nullable=True)
    theForm = Column(String, nullable=True)
    formkey = Column(String(32), nullable=True)

class FormsFields(Base):
    __tablename__ = "Forms_Fields"
    formID = Column(Integer, primary_key=True)
    fieldID = Column(Integer)
    required = Column(Boolean, nullable=True)
    sortnum = Column(SmallInteger)

class FormsFieldsOptions(Base):
    __tablename__ = "Forms_Fields_Options"
    optionID = Column(Integer, primary_key=True)
    fieldID = Column(Integer, nullable=True)
    selOption = Column(String(100), nullable=True)
    sortnum = Column(SmallInteger, nullable=True)

class FormsFieldsSource(Base):
    __tablename__ = "Forms_Fields_Source"
    fieldID = Column(Integer, primary_key=True)
    depID = Column(Integer, nullable=True)
    predef = Column(SmallInteger)
    fieldname = Column(String(100), nullable=True)
    fieldlabel = Column(String(100))
    fieldTypeID = Column(Integer)
    fieldDescr = Column(String(100), nullable=True)
    maxchars = Column(SmallInteger, nullable=True)
    fieldwidth = Column(String, nullable=True)
    arearows = Column(SmallInteger, nullable=True)

class FormsFieldtypes(Base):
    __tablename__ = "Forms_FieldTypes"
    fieldTypeID = Column(Integer, primary_key=True)
    fieldType = Column(String(30), nullable=True)
    preDef = Column(Boolean, nullable=True)
    descr = Column(String(50), nullable=True)
    sort = Column(SmallInteger, nullable=True)
    boolShow = Column(Boolean, nullable=True)
    defFunction = Column(String(20), nullable=True)

class FormsReceived(Base):
    __tablename__ = "Forms_Received"
    recID = Column(Integer, primary_key=True)
    form = Column(String(50))
    sender_lname = Column(String(50), nullable=True)
    sender_fname = Column(String(50), nullable=True)
    sender_email = Column(String(100), nullable=True)
    to_mail = Column(String(100), nullable=True)
    formContent = Column(String, nullable=True)
    formKey = Column(String(32), nullable=True)
    date_created = Column(DateTime)

class FormsTypes(Base):
    __tablename__ = "Forms_Types"
    formType = Column(Integer, primary_key=True)
    typename = Column(String(50))

class ImagesCcond(Base):
    __tablename__ = "Images_Ccond"
    imageID = Column(Integer, primary_key=True)
    imagefile = Column(String(250), nullable=True)
    date_created = Column(DateTime, nullable=True)

class ImagesProfiles(Base):
    __tablename__ = "Images_Profiles"
    imageID = Column(Integer, primary_key=True)
    imagepath = Column(String(100), nullable=True)
    imagefile = Column(String(100), nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    date_created = Column(DateTime)

class ImagesSlider(Base):
    __tablename__ = "Images_Slider"
    imageID = Column(Integer, primary_key=True)
    imagefile = Column(String(250), nullable=True)
    date_created = Column(DateTime, nullable=True)
    depID = Column(Integer, nullable=True)

class MembersChange(Base):
    __tablename__ = "Members_Change"
    recID = Column(Integer, primary_key=True)
    membernum = Column(String(50), nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    memberemail = Column(String(100), nullable=True)
    cat_old = Column(String(100), nullable=True)
    cat_new = Column(String(100), nullable=True)
    comments = Column(String(1000), nullable=True)
    formkey = Column(String(32), nullable=True)
    terms = Column(String, nullable=True)
    terms_extra = Column(String(1000), nullable=True)
    boolDeleted = Column(Boolean, nullable=True)
    date_created = Column(DateTime, nullable=True)
    famMembers = Column(String(200), nullable=True)

class MembersIn(Base):
    __tablename__ = "Members_In"
    recID = Column(Integer, primary_key=True)
    orderID = Column(Integer, nullable=True)
    orderConfirmed = Column(Boolean, nullable=True)
    born = Column(String(20), nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    membAddress = Column(String(100), nullable=True)
    pcodecity = Column(String(100), nullable=True)
    fromEmail = Column(String(100), nullable=True)
    phone = Column(String(20), nullable=True)
    parentname = Column(String(100), nullable=True)
    parentphone = Column(String(30), nullable=True)
    parentemail = Column(String(100), nullable=True)
    hcp = Column(String(6), nullable=True)
    membOtherClub = Column(String(3), nullable=True)
    otherClubname = Column(String(500), nullable=True)
    boolHomeclub = Column(String(3), nullable=True)
    boolEcoDue = Column(String(3), nullable=True)
    houseMagazine = Column(String(3), nullable=True)
    wishMagazine = Column(String(3), nullable=True)
    membercat = Column(String(200), nullable=True)
    familyRelations = Column(String(1000), nullable=True)
    extra_1 = Column(String(100), nullable=True)
    extra_2 = Column(String(100), nullable=True)
    extra_3 = Column(String(100), nullable=True)
    comments = Column(String(3000), nullable=True)
    formkey = Column(String(32), nullable=True)
    date_created = Column(DateTime, nullable=True)
    boolDeleted = Column(Boolean, nullable=True)
    terms = Column(String, nullable=True)
    payPeriode = Column(String(20), nullable=True)
    terms_extra = Column(String(1000), nullable=True)
    vtgCourse = Column(String(3), nullable=True)
    vtgClub = Column(String(100), nullable=True)
    gender = Column(String(10), nullable=True)
    vtgYear = Column(String(10), nullable=True)
    otherMembernum = Column(String(30), nullable=True)
    boolAdult = Column(Boolean, nullable=True)
    vtgID = Column(Integer, nullable=True)
    categoryID = Column(Integer, nullable=True)
    otherClubMemberNum = Column(String(30), nullable=True)
    familyMembership = Column(Boolean, nullable=True)
    customerclub = Column(String(4), nullable=True)
    participantID_vtg = Column(Integer, nullable=True)
    borndate = Column(Date, nullable=True)
    junOrgTraining = Column(String(5), nullable=True)

class MembersOut(Base):
    __tablename__ = "Members_Out"
    recID = Column(Integer, primary_key=True)
    membernum = Column(String(20), nullable=True)
    firstname = Column(String(50), nullable=True)
    lastname = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True)
    comments = Column(String(1000), nullable=True)
    formkey = Column(String(32), nullable=True)
    contactMe = Column(String(5), nullable=True)
    date_created = Column(DateTime, nullable=True)
    boolDeleted = Column(Boolean, nullable=True)
    reason = Column(String(100), nullable=True)
    supportMember = Column(String(4), nullable=True)

class MembersSignoutSource(Base):
    __tablename__ = "Members_SignOut_Source"
    fieldID = Column(Integer, primary_key=True)
    fieldname = Column(String(30))
    fieldtype = Column(Integer, nullable=True)
    fieldExplain = Column(String(100), nullable=True)
    boolShow = Column(Boolean)
    boolActive = Column(Boolean, nullable=True)
    db_col = Column(String(50), nullable=True)
    field_html = Column(String(1000), nullable=True)
    sortnum = Column(SmallInteger, nullable=True)

class MembersSignupSource(Base):
    __tablename__ = "Members_Signup_Source"
    fieldID = Column(Integer, primary_key=True)
    fieldname = Column(String(50))
    fieldtype = Column(Integer, nullable=True)
    fieldExplain = Column(String(100), nullable=True)
    boolShow = Column(Boolean)
    boolActive = Column(Boolean, nullable=True)
    db_col = Column(String(50), nullable=True)
    field_html = Column(String(1000), nullable=True)
    sortnum = Column(SmallInteger, nullable=True)

class Memberships(Base):
    __tablename__ = "Memberships"
    categoryID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean, nullable=True)
    category = Column(String(100))
    sortnum = Column(SmallInteger)
    catprice = Column(DECIMAL, nullable=True)
    price_quota = Column(String(10), nullable=True)
    catdescription = Column(String(2000), nullable=True)
    date_created = Column(DateTime)
    created_by = Column(String(100), nullable=True)
    boolTerms = Column(Boolean, nullable=True)
    catterms = Column(String(1000), nullable=True)
    boolFamily = Column(Boolean, nullable=True)
    catmail = Column(String(1000), nullable=True)
    boolCatmail = Column(Boolean, nullable=True)
    catprice_month = Column(DECIMAL, nullable=True)
    catprice_year = Column(DECIMAL, nullable=True)
    show_priceMonth = Column(Boolean, nullable=True)
    show_priceYear = Column(Boolean, nullable=True)
    boolSelInVtg = Column(Boolean, nullable=True)
    boolSelectSignup = Column(Boolean, nullable=True)
    boolSelectChangecat = Column(Boolean, nullable=True)

class MembershipsVtg(Base):
    __tablename__ = "Memberships_Vtg"
    vtgListID = Column(Integer, primary_key=True)
    membercatID = Column(Integer)

class MenuMain(Base):
    __tablename__ = "Menu_Main"
    itemID = Column(Integer, primary_key=True)
    parentID = Column(Integer, nullable=True)
    boolShow = Column(Boolean)
    boolNewWin = Column(Boolean)
    sortnum = Column(SmallInteger)
    item = Column(String(100))
    itemlink = Column(String(250))
    icon = Column(String(30), nullable=True)

class NewsArticlesPlugins(Base):
    __tablename__ = "News_Articles_Plugins"
    articleID = Column(Integer, primary_key=True)
    pluginID = Column(Integer)
    pluginRef = Column(Integer)

class NewsBulletins(Base):
    __tablename__ = "News_Bulletins"
    articleID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    boolShow = Column(Boolean)
    heading = Column(String(100))
    urlTitle = Column(String(200))
    indexImageID = Column(Integer, nullable=True)
    indexImage = Column(String(100), nullable=True)
    indexImagePath = Column(String(200), nullable=True)
    indeximg_descr = Column(String(500), nullable=True)
    newscontent = Column(String(5000), nullable=True)
    pagedescription = Column(String(500), nullable=True)
    date_published = Column(DateTime, nullable=True)
    date_created = Column(DateTime)
    created_by = Column(String(100), nullable=True)
    date_modified = Column(DateTime, nullable=True)
    modified_by = Column(String(100), nullable=True)

class NewsKeywords(Base):
    __tablename__ = "News_Keywords"
    keyword = Column(String(25), primary_key=True)
    numSearch = Column(Integer, nullable=True)

class Orderdetails(Base):
    __tablename__ = "OrderDetails"
    orderID = Column(Integer, primary_key=True)
    productID = Column(Integer, nullable=True)
    productNumber = Column(String(100), nullable=True)
    productName = Column(String(100), nullable=True)
    prodVarID = Column(Integer, nullable=True)
    activityID = Column(Integer, nullable=True)
    activityName = Column(String(100), nullable=True)
    tournID = Column(Integer, nullable=True)
    tournName = Column(String(100), nullable=True)
    participantID = Column(Integer, nullable=True)
    feedbackID = Column(Integer, nullable=True)
    feedbackName = Column(String(100), nullable=True)
    senderID = Column(Integer, nullable=True)
    spec = Column(String(200), nullable=True)
    textspec = Column(String(200), nullable=True)
    quantity = Column(Integer)
    unitprice = Column(DECIMAL)
    taxPros = Column(SmallInteger, nullable=True)
    subtotal = Column(DECIMAL, nullable=True)
    memberRecID = Column(Integer, nullable=True)

class Orders(Base):
    __tablename__ = "Orders"
    orderID = Column(Integer, primary_key=True)
    orderNum = Column(String(20), nullable=True)
    paymentRef = Column(String(50), nullable=True)
    payType = Column(String(50), nullable=True)
    payMethod = Column(String(50), nullable=True)
    maskedPan = Column(String(50), nullable=True)
    cartID = Column(String(50), nullable=True)
    customerID = Column(Integer, nullable=True)
    custFname = Column(String(50), nullable=True)
    custSname = Column(String(50), nullable=True)
    custCompany = Column(String(100), nullable=True)
    custAddress = Column(String(300), nullable=True)
    custPostcode = Column(String(10), nullable=True)
    custTown = Column(String(50), nullable=True)
    custEmail = Column(String(100), nullable=True)
    custPhone = Column(String(50), nullable=True)
    custComments = Column(String(1000), nullable=True)
    shippingMethod = Column(String(100), nullable=True)
    shippingPrice = Column(DECIMAL, nullable=True)
    admFee = Column(DECIMAL, nullable=True)
    admFeeDescription = Column(String(200), nullable=True)
    boolCancelled = Column(Boolean)
    orderKey = Column(String(50), nullable=True)
    confirmKey = Column(String(50), nullable=True)
    dateCreated = Column(DateTime)
    boolCustConfirmed = Column(Boolean)
    dateCustConfirmed = Column(DateTime, nullable=True)
    boolShipped = Column(Boolean)
    dateShipped = Column(DateTime, nullable=True)
    boolClosed = Column(Boolean)
    dateClosed = Column(DateTime, nullable=True)
    closed_by = Column(String(100), nullable=True)
    cancelled_by = Column(String(100), nullable=True)
    sysComments = Column(String(100), nullable=True)
    amountCharged = Column(DECIMAL, nullable=True)
    amountReserved = Column(DECIMAL, nullable=True)
    trigger_Webhook = Column(DateTime, nullable=True)
    reservedAmount = Column(DECIMAL, nullable=True)
    chargedAmount = Column(DECIMAL, nullable=True)
    chargeID = Column(String(50), nullable=True)
    chargeDate = Column(DateTime, nullable=True)
    boolPaymentConfirmed = Column(Boolean, nullable=True)
    datePaymentConfirmed = Column(DateTime, nullable=True)
    boolEmailReceipt = Column(Boolean, nullable=True)
    payAccount = Column(Integer, nullable=True)
    payLocal = Column(Boolean, nullable=True)
    boolRefunded = Column(Boolean, nullable=True)
    refundRef = Column(String(50), nullable=True)
    refundAmount = Column(DECIMAL, nullable=True)
    refundDate = Column(DateTime, nullable=True)

class Pages(Base):
    __tablename__ = "Pages"
    pageID = Column(Integer, primary_key=True)
    parentID = Column(Integer, nullable=True)
    depID = Column(Integer)
    menuID = Column(Integer, nullable=True)
    boolArchive = Column(Boolean, nullable=True)
    pluginID = Column(Integer, nullable=True)
    plugin_ref = Column(String(10), nullable=True)
    functionID = Column(Integer, nullable=True)
    functionRef = Column(String(10), nullable=True)
    fRefAlias = Column(String(200), nullable=True)
    boolStart = Column(Boolean)
    boolShow = Column(Boolean)
    boolShowinmega = Column(Boolean, nullable=True)
    boolPrivacy = Column(Boolean, nullable=True)
    sortnum = Column(SmallInteger)
    template = Column(SmallInteger, nullable=True)
    templateID = Column(SmallInteger, nullable=True)
    boolImgZoom = Column(Boolean, nullable=True)
    boolDirectLink = Column(Boolean)
    directLink = Column(String(200), nullable=True)
    boolExtLink = Column(Boolean)
    validfrom = Column(DateTime)
    validto = Column(DateTime)
    pagename = Column(String(100))
    pagedescription = Column(String(500), nullable=True)
    indexImageID = Column(Integer, nullable=True)
    indexImage = Column(String(100), nullable=True)
    indexImagePath = Column(String(200), nullable=True)
    indeximg_descr = Column(String(500), nullable=True)
    templateImageID = Column(Integer, nullable=True)
    templateImage = Column(String(200), nullable=True)
    templimg_descr = Column(String(500), nullable=True)
    urlTitle = Column(String(200))
    pageheading = Column(String(200))
    pagecontent = Column(String, nullable=True)
    date_created = Column(DateTime)
    created_by = Column(String(100))
    date_modified = Column(DateTime, nullable=True)
    modified_by = Column(String(100), nullable=True)
    videoUrl = Column(String(200), nullable=True)
    teaser = Column(String(500), nullable=True)
    boolInfoscreen = Column(Boolean, nullable=True)
    boolArchived = Column(Boolean, nullable=True)
    template_bgcolor = Column(String(100), nullable=True)
    pageurlname = Column(String(255), nullable=True)
    headerImage = Column(String(100), nullable=True)

class PagesMenus(Base):
    __tablename__ = "Pages_Menus"
    menuID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    boolShow = Column(Boolean)
    menuheading = Column(String(50))
    sortnum = Column(SmallInteger)
    date_created = Column(DateTime)
    created_by = Column(String(100), nullable=True)

class PagesPlugins(Base):
    __tablename__ = "Pages_Plugins"
    pageID = Column(Integer, primary_key=True, nullable=True)
    articleID = Column(Integer, nullable=True)
    pluginID = Column(Integer)
    pluginRef = Column(Integer)

class Payment(Base):
    __tablename__ = "Payment"
    orgnummer = Column(String(20), primary_key=True, nullable=True)
    boolOrdertoEmail = Column(Boolean)
    emailOrders = Column(String(50), nullable=True)
    boolDibs = Column(Boolean)
    DibsMerchantID = Column(String(20), nullable=True)
    Dibs_description = Column(String(100), nullable=True)
    feeDibs = Column(DECIMAL, nullable=True)
    Dibs_test = Column(Boolean, nullable=True)
    boolKlarna_invoice = Column(Boolean)
    boolKlarna_account = Column(Boolean)
    KlarnaMerchantID = Column(String(20), nullable=True)
    KlarnaSecret = Column(String(20), nullable=True)
    feeKlarna_invoice = Column(DECIMAL, nullable=True)
    Klarna_inv_description = Column(String(100), nullable=True)
    feeKlarna_account = Column(DECIMAL, nullable=True)
    Klarna_acc_description = Column(String(100), nullable=True)
    boolLocalhandling = Column(Boolean)
    feeLocalhandling = Column(DECIMAL, nullable=True)
    Local_description = Column(String(200), nullable=True)
    terms = Column(String, nullable=True)

class Photoalbum(Base):
    __tablename__ = "Photoalbum"
    categoryID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    boolShow = Column(Boolean)
    albumname = Column(String(100))
    urlAlias = Column(String(200))
    sortnum = Column(String)
    date_created = Column(DateTime)
    created_by = Column(String(50), nullable=True)

class PhotoalbumImages(Base):
    __tablename__ = "Photoalbum_Images"
    imageID = Column(Integer, primary_key=True)
    categoryID = Column(Integer)
    boolShow = Column(Boolean)
    imagefile = Column(String(50))
    imgWidth = Column(String(4), nullable=True)
    imgHeight = Column(String(4), nullable=True)
    imgDescription = Column(String(200), nullable=True)
    sortnum = Column(String)

class Plugins(Base):
    __tablename__ = "Plugins"
    pluginID = Column(Integer, primary_key=True)
    pluginPagefile = Column(String(50))
    pluginFunction = Column(String(50))
    pluginName = Column(String(50), nullable=True)
    pluginMain = Column(String(50), nullable=True)
    areaID = Column(Integer, nullable=True)
    categoryID = Column(Integer, nullable=True)
    sortnum = Column(SmallInteger, nullable=True)
    superv = Column(Boolean, nullable=True)

class PluginsCategories(Base):
    __tablename__ = "Plugins_Categories"
    categoryID = Column(Integer, primary_key=True)
    pluginCat = Column(String(30))

class Profiles(Base):
    __tablename__ = "Profiles"
    profileID = Column(Integer, primary_key=True)
    firstname = Column(String(50))
    lastname = Column(String(50))
    imageID = Column(Integer, nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(50), nullable=True)
    descr = Column(String(500), nullable=True)
    myFacebook = Column(String(200), nullable=True)
    myInsta = Column(String(200), nullable=True)
    myScangolf = Column(String(200), nullable=True)
    myLinkedin = Column(String(200), nullable=True)
    myTwitter = Column(String(200), nullable=True)
    myYoutube = Column(String(200), nullable=True)
    date_created = Column(DateTime, nullable=True)
    created_by = Column(String(100), nullable=True)

class SetupBasic(Base):
    __tablename__ = "Setup_Basic"
    clubname = Column(String(50), primary_key=True)
    address = Column(String(100), nullable=True)
    postcode = Column(String(8), nullable=True)
    city = Column(String(30), nullable=True)
    orgnr = Column(String(20), nullable=True)
    longitude = Column(String(20), nullable=True)
    latitude = Column(String(20), nullable=True)
    urlContact = Column(String(100), nullable=True)
    defibrillator = Column(Boolean, nullable=True)
    memberSignupTo = Column(String(100), nullable=True)
    memberSignupTo_cc = Column(String(200), nullable=True)
    memberTerms = Column(String(2000), nullable=True)
    memberOnlinePay = Column(Boolean, nullable=True)
    course_condition = Column(String(3000), nullable=True)
    ccond_url = Column(String(200), nullable=True)
    ccond_image = Column(String(100), nullable=True)
    ccond_validfrom = Column(Date, nullable=True)
    ccond_validto = Column(Date, nullable=True)
    blogDescr = Column(String(300), nullable=True)
    blogNumInWidget = Column(SmallInteger, nullable=True)
    extraMailMsg = Column(String(5000), nullable=True)
    memberSelPayPeriode = Column(Boolean, nullable=True)
    geoHeight = Column(String(4), nullable=True)
    ccon_selreport = Column(String(20), nullable=True)
    ccon_rssurl = Column(String(255), nullable=True)

class SetupBasicReceivers(Base):
    __tablename__ = "Setup_Basic_Receivers"
    recID = Column(Integer, primary_key=True)
    receiver = Column(String(100))
    phone = Column(String(100), nullable=True)
    email = Column(String(100), nullable=True)
    sortnum = Column(SmallInteger)
    mainContact = Column(Boolean, nullable=True)

class SetupLanguage(Base):
    __tablename__ = "Setup_Language"
    langCode = Column(String(10), primary_key=True)
    language = Column(String(30))
    localurl = Column(String(250), nullable=True)

class SetupPayment(Base):
    __tablename__ = "Setup_Payment"
    email_orders = Column(String(100), primary_key=True, nullable=True)
    email_orders_cc = Column(String(100), nullable=True)
    boolLocal = Column(Boolean, nullable=True)
    localDescr = Column(String(100), nullable=True)
    local_fee = Column(DECIMAL, nullable=True)
    boolNets = Column(Boolean)
    Nets_testmodus = Column(Boolean, nullable=True)
    Nets_merchantID = Column(String(50), nullable=True)
    Nets_secretkey_live = Column(String(100), nullable=True)
    Nets_checkoutkey_live = Column(String(100), nullable=True)
    Nets_secretkey_test = Column(String(100), nullable=True)
    Nets_checkoutkey_test = Column(String(100), nullable=True)
    terms = Column(String, nullable=True)
    boolCharge = Column(Boolean, nullable=True)
    accID = Column(Integer)
    accountName = Column(String(100), nullable=True)
    companyAdr = Column(String(100), nullable=True)
    pcode = Column(String(10), nullable=True)
    city = Column(String(100), nullable=True)
    orgnr = Column(String(20), nullable=True)
    boolOrder_byemail = Column(Boolean, nullable=True)

class SetupSite(Base):
    __tablename__ = "Setup_Site"
    amtNewsMainFront = Column(SmallInteger, primary_key=True)
    amtNewsDepFront = Column(SmallInteger, nullable=True)
    amtNewsPri = Column(SmallInteger, nullable=True)
    newsPriBig = Column(Boolean, nullable=True)
    siteDescription = Column(String(200), nullable=True)
    fb_Url = Column(String(200), nullable=True)
    fb_AppId = Column(String(20), nullable=True)
    fb_AdminID = Column(String(20), nullable=True)
    fb_AppSecret = Column(String(32), nullable=True)
    fb_pixelID = Column(String(30), nullable=True)
    google_Verification = Column(String(100), nullable=True)
    google_AnalyticsID = Column(String(30), nullable=True)
    google_API_KEY = Column(String(100), nullable=True)
    insta_Url = Column(String(200), nullable=True)
    twitter_Url = Column(String(200), nullable=True)
    youtube_Url = Column(String(200), nullable=True)
    snapchat_Url = Column(String(200), nullable=True)
    topLanguage = Column(Boolean, nullable=True)
    topSearch = Column(Boolean, nullable=True)
    topUser = Column(Boolean, nullable=True)
    topSocial = Column(Boolean, nullable=True)
    topWeather = Column(Boolean, nullable=True)
    weather_url = Column(String(250), nullable=True)
    spotify_Url = Column(String(200), nullable=True)
    google_Tagmanager = Column(String(30), nullable=True)
    title_front = Column(String(200), nullable=True)
    yr_url = Column(String(200), nullable=True)
    googleMapCode = Column(String(1000), nullable=True)
    longitude = Column(String(30), nullable=True)
    latitude = Column(String(30), nullable=True)
    geoHeight = Column(String(4), nullable=True)
    yr_widgetBG = Column(String(10), nullable=True)
    hioOnlyYear = Column(Boolean, nullable=True)
    linkedIn_Url = Column(String(200), nullable=True)
    newsTemplate = Column(SmallInteger, nullable=True)
    useInfoscreen = Column(Boolean, nullable=True)
    fb_PageID = Column(String(30), nullable=True)
    useCSbooking = Column(Boolean, nullable=True)

class ShopCategories(Base):
    __tablename__ = "Shop_Categories"
    categoryID = Column(Integer, primary_key=True)
    category = Column(String(50), nullable=True)
    boolShow = Column(Boolean)
    urlAlias = Column(String(50))
    sortnum = Column(SmallInteger)

class ShopProducts(Base):
    __tablename__ = "Shop_Products"
    productID = Column(Integer, primary_key=True)
    parentID = Column(Integer, nullable=True)
    boolExpired = Column(Boolean, nullable=True)
    boolShow = Column(Boolean)
    boolForSale = Column(Boolean)
    boolVariants = Column(Boolean)
    boolTextvariant = Column(Boolean)
    boolLimitOne = Column(Boolean, nullable=True)
    boolShipping = Column(Boolean, nullable=True)
    custSpecText = Column(String(30), nullable=True)
    sortnum = Column(String, nullable=True)
    pricePrefix = Column(String(1), nullable=True)
    priceOffset = Column(DECIMAL, nullable=True)
    textvarlabel = Column(String(200), nullable=True)
    boolTextvarRequired = Column(Boolean)
    productName = Column(String(100), nullable=True)
    variant = Column(String(100), nullable=True)
    urlAlias = Column(String(70), nullable=True)
    taxCode = Column(SmallInteger, nullable=True)
    price = Column(DECIMAL, nullable=True)
    price_std = Column(DECIMAL)
    boolPrice_camp = Column(Boolean, nullable=True)
    price_camp = Column(DECIMAL, nullable=True)
    campFromdate = Column(DateTime, nullable=True)
    campTodate = Column(DateTime, nullable=True)
    stock = Column(String, nullable=True)
    shortdescr = Column(String(200), nullable=True)
    description = Column(String, nullable=True)
    datereg = Column(DateTime)
    creator = Column(String(100), nullable=True)
    categoryID = Column(Integer, nullable=True)
    boolLocalSaleOnly = Column(Boolean, nullable=True)

class ShopProductsImages(Base):
    __tablename__ = "Shop_Products_Images"
    imageID = Column(Integer, primary_key=True)
    productID = Column(Integer)
    imagefile = Column(String(200))
    sortnum = Column(SmallInteger)
    imgDescription = Column(String(100), nullable=True)

class ShopProductvargroup(Base):
    __tablename__ = "Shop_ProductVargroup"
    productID = Column(Integer, primary_key=True)
    vargroupID = Column(Integer)

class ShopSetup(Base):
    __tablename__ = "Shop_Setup"
    boolCategories = Column(Boolean, primary_key=True, nullable=True)
    payment_Nets = Column(Boolean, nullable=True)
    payment_Local = Column(Boolean, nullable=True)
    payment_Local_Descr = Column(String(50), nullable=True)
    mailMessage = Column(String(1000), nullable=True)

class ShopShippings(Base):
    __tablename__ = "Shop_Shippings"
    shippingID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean)
    shippingMethod = Column(String(100))
    price = Column(DECIMAL)
    sortnum = Column(SmallInteger, nullable=True)

class ShopVargroups(Base):
    __tablename__ = "Shop_Vargroups"
    varGroupID = Column(Integer, primary_key=True)
    groupname = Column(String(30), nullable=True)

class SimTournamentScore(Base):
    __tablename__ = "Sim_Tournament_Score"
    scoreID = Column(Integer, primary_key=True)
    tournID = Column(Integer, nullable=True)
    playerID = Column(Integer, nullable=True)
    hcp = Column(Float, nullable=True)
    netto = Column(SmallInteger, nullable=True)
    brutto = Column(SmallInteger, nullable=True)

class SimTournamentSignups(Base):
    __tablename__ = "Sim_Tournament_Signups"
    signupID = Column(Integer, primary_key=True)
    playerID = Column(Integer, nullable=True)
    tournID = Column(Integer, nullable=True)
    firstname = Column(String(30), nullable=True)
    lastname = Column(String(50), nullable=True)
    email = Column(String(100), nullable=True)
    phone = Column(String(30), nullable=True)
    onWaitlist = Column(Boolean, nullable=True)

class SimTournaments(Base):
    __tablename__ = "Sim_Tournaments"
    tournID = Column(Integer, primary_key=True)
    tourID = Column(Integer, nullable=True)
    boolShow = Column(Boolean, nullable=True)
    tournname = Column(String(100), nullable=True)
    urlTitle = Column(String(250), nullable=True)
    tourndate = Column(Date, nullable=True)
    time_from = Column(String(4), nullable=True)
    coursename = Column(String(100), nullable=True)
    maxParticipants = Column(String, nullable=True)
    partReserved = Column(String, nullable=True)
    tournDescription = Column(String, nullable=True)
    boolWaitlist = Column(Boolean, nullable=True)
    signup_from = Column(DateTime, nullable=True)
    signup_to = Column(DateTime, nullable=True)
    boolTeeTimePubl = Column(Boolean, nullable=True)
    boolResPubl = Column(Boolean, nullable=True)

class SimTourplayers(Base):
    __tablename__ = "Sim_TourPlayers"
    playerID = Column(Integer, primary_key=True)
    tourID = Column(Integer, nullable=True)
    firstname = Column(String(30), nullable=True)
    lastname = Column(String(50), nullable=True)
    hcp = Column(Float, nullable=True)

class SimTours(Base):
    __tablename__ = "Sim_Tours"
    tourID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    tourname = Column(String(100))
    urlTitle = Column(String(250), nullable=True)
    boolShow = Column(Boolean, nullable=True)
    sortnum = Column(SmallInteger, nullable=True)

class SiteusersPwdtemp(Base):
    __tablename__ = "Siteusers_PwdTemp"
    username = Column(String(50), primary_key=True)
    useremail = Column(String(50))
    pwdkey = Column(String(32))
    date_valid = Column(DateTime)

class SiteusersSubscr(Base):
    __tablename__ = "Siteusers_Subscr"
    userID = Column(Integer, primary_key=True)
    depID = Column(Integer)

class Sponsors(Base):
    __tablename__ = "Sponsors"
    sponsorID = Column(Integer, primary_key=True)
    boolShow = Column(Boolean)
    sponsor = Column(String(50))
    logofile = Column(String(50), nullable=True)
    url = Column(String(200), nullable=True)
    sortnum = Column(SmallInteger)
    sponsorDescr = Column(String(3000), nullable=True)
    categoryID = Column(Integer, nullable=True)

class SponsorsCategories(Base):
    __tablename__ = "Sponsors_Categories"
    categoryID = Column(Integer, primary_key=True)
    category = Column(String(50))
    sortnum = Column(SmallInteger)
    boolPri = Column(Boolean, nullable=True)
    sizecat = Column(SmallInteger, nullable=True)

class StatusCourseclub(Base):
    __tablename__ = "Status_CourseClub"
    boolCourse9 = Column(Boolean, primary_key=True, nullable=True)
    txtCourse9 = Column(String(50), nullable=True)
    boolSimCenter = Column(Boolean, nullable=True)
    txtSimCenter = Column(String(50), nullable=True)
    boolRange = Column(Boolean, nullable=True)
    txtRange = Column(String(50), nullable=True)
    boolPracticeOut = Column(Boolean, nullable=True)
    txtPracticeOut = Column(String(50), nullable=True)
    boolPracticeIn = Column(Boolean, nullable=True)
    txtPracticeIn = Column(String(50), nullable=True)
    boolPracticeGreen = Column(Boolean, nullable=True)
    txtPracticeGreen = Column(String(50), nullable=True)
    selGreenQ = Column(String(30), nullable=True)
    txtGreenQ = Column(String(50), nullable=True)
    boolBallplacing = Column(Boolean, nullable=True)
    txtBallplacing = Column(String(50), nullable=True)
    boolLessons = Column(Boolean, nullable=True)
    txtLessons = Column(String(50), nullable=True)
    boolCafe = Column(Boolean, nullable=True)
    txtCafe = Column(String(50), nullable=True)
    boolShop = Column(Boolean, nullable=True)
    txtShop = Column(String(50), nullable=True)
    boolKiosk = Column(Boolean, nullable=True)
    txtKiosk = Column(String(50), nullable=True)
    boolOffice = Column(Boolean, nullable=True)
    txtOffice = Column(String(50), nullable=True)

class StatusInfo(Base):
    __tablename__ = "Status_Info"
    statusID = Column(Integer, primary_key=True)
    statusLabel = Column(String(30), nullable=True)
    boolOpen = Column(Boolean, nullable=True)
    statusText = Column(String(100), nullable=True)
    sortnum = Column(SmallInteger, nullable=True)

class Taxcodes(Base):
    __tablename__ = "Taxcodes"
    taxCode = Column(Integer, primary_key=True)
    taxPros = Column(SmallInteger)

class TemplateContent(Base):
    __tablename__ = "Template_Content"
    templateID = Column(SmallInteger, primary_key=True)
    template = Column(String(50), nullable=True)
    col_left = Column(String(30), nullable=True)
    col_right = Column(String(30), nullable=True)

class TourPlayers(Base):
    __tablename__ = "Tour_Players"
    recID = Column(Integer, primary_key=True)
    tourID = Column(Integer)
    tournID = Column(Integer)
    playerID = Column(Integer)
    firstname = Column(String(30), nullable=True)
    lastname = Column(String(50), nullable=True)
    hcp = Column(Float)

class TourScores(Base):
    __tablename__ = "Tour_Scores"
    scoreID = Column(Integer, primary_key=True)
    tourID = Column(Integer, nullable=True)
    tournID = Column(Integer)
    playerID = Column(Integer)
    par = Column(SmallInteger)
    hcp = Column(Float)
    brutto = Column(SmallInteger)
    netto = Column(SmallInteger, nullable=True)
    points = Column(SmallInteger, nullable=True)

class Tournaments(Base):
    __tablename__ = "Tournaments"
    tournID = Column(Integer, primary_key=True)
    listID = Column(Integer)
    tourID = Column(Integer, nullable=True)
    boolShow = Column(Boolean)
    tournName = Column(String(100))
    tournAlias = Column(String(100), nullable=True)
    location = Column(String(200), nullable=True)
    tournDescription = Column(String, nullable=True)
    date_start = Column(DateTime, nullable=True)
    time_from = Column(String(4))
    time_to = Column(String(4))
    boolGolfboxSignup = Column(Boolean)
    gbTournID = Column(Integer, nullable=True)
    boolOnlineSignup = Column(Boolean)
    formID = Column(Integer, nullable=True)
    boolOnlinePay = Column(Boolean)
    boolWaitlist = Column(Boolean, nullable=True)
    maxParticipants = Column(String, nullable=True)
    partReserved = Column(String, nullable=True)
    signup_from = Column(DateTime, nullable=True)
    signup_to = Column(DateTime, nullable=True)
    boolSuCouple = Column(Boolean)
    boolSuTeetime = Column(Boolean)
    boolSuHomeclub = Column(Boolean)
    boolSuPhone = Column(Boolean)
    boolSuBornyear = Column(Boolean)
    boolSignupToMail = Column(Boolean)
    signupMailTo = Column(String(50), nullable=True)
    date_created = Column(DateTime)
    boolTeeTimePubl = Column(Boolean)
    teeTimeLink = Column(String(250), nullable=True)
    boolTeeTimeLinkExt = Column(Boolean)
    boolResPubl = Column(Boolean)
    resLink = Column(String(250), nullable=True)
    boolResLinkExt = Column(Boolean)
    refnr = Column(String(6), nullable=True)
    created_by = Column(String(100))
    boolExternal = Column(Boolean, nullable=True)
    priceGroupID = Column(Integer, nullable=True)
    boolSuHcp = Column(Boolean, nullable=True)
    boolSuMembernum = Column(Boolean, nullable=True)
    boolShowSignups = Column(Boolean, nullable=True)

class TournamentsList(Base):
    __tablename__ = "Tournaments_List"
    listID = Column(Integer, primary_key=True)
    depID = Column(Integer)
    sortnum = Column(SmallInteger)
    tourID = Column(Integer, nullable=True)
    listname = Column(String(100))
    urlTitle = Column(String(200), nullable=True)
    listDescription = Column(String(2000), nullable=True)
    listYear = Column(String(4), nullable=True)
    gb_customerid = Column(String(20), nullable=True)
    boolGbList = Column(Boolean)
    gbListUrl = Column(String(300), nullable=True)
    boolShow = Column(Boolean)
    date_created = Column(DateTime)
    created_by = Column(String(50))
    listFilter = Column(String(10), nullable=True)
    gbListID = Column(String(10), nullable=True)

class TournamentsParticipants(Base):
    __tablename__ = "Tournaments_Participants"
    participantID = Column(Integer, primary_key=True)
    tournID = Column(Integer)
    boolSuConfirmed = Column(Boolean)
    orderID = Column(Integer, nullable=True)
    price = Column(DECIMAL, nullable=True)
    memberID = Column(String(30), nullable=True)
    hcp = Column(String(10), nullable=True)
    fname = Column(String(50))
    sname = Column(String(50))
    email = Column(String(100))
    bornYear = Column(String(4), nullable=True)
    telephone = Column(String(50), nullable=True)
    homeClub = Column(String(50), nullable=True)
    memberID_mark = Column(String(30), nullable=True)
    fname_mark = Column(String(50), nullable=True)
    sname_mark = Column(String(50), nullable=True)
    bornYear_mark = Column(String(4), nullable=True)
    hcp_mark = Column(String(10), nullable=True)
    homeClub_mark = Column(String(50), nullable=True)
    suTeeTime = Column(String(20), nullable=True)
    comments = Column(String(500), nullable=True)
    suVerified = Column(Boolean)
    onWaitlist = Column(Boolean, nullable=True)
    refnr = Column(String(6), nullable=True)
    date_signup = Column(DateTime, nullable=True)

class TournamentsResults(Base):
    __tablename__ = "Tournaments_Results"
    tournID = Column(Integer, primary_key=True)
    boolHtml = Column(Boolean)
    result = Column(String, nullable=True)
    created_by = Column(String(100), nullable=True)

class TournamentsScore(Base):
    __tablename__ = "Tournaments_Score"
    scoreID = Column(Integer, primary_key=True)
    tournID = Column(Integer, nullable=True)
    playerID = Column(Integer, nullable=True)
    hcp = Column(Float, nullable=True)
    netto = Column(SmallInteger, nullable=True)
    brutto = Column(SmallInteger, nullable=True)

class TournamentsStartlists(Base):
    __tablename__ = "Tournaments_Startlists"
    tournID = Column(Integer, primary_key=True)
    boolHtml = Column(Boolean)
    startlist = Column(String, nullable=True)
    created_by = Column(String(100), nullable=True)

class Widgets(Base):
    __tablename__ = "Widgets"
    widgetID = Column(Integer, primary_key=True)
    depID = Column(Integer, nullable=True)
    widgetWidth = Column(String(1), nullable=True)
    widgetName = Column(String(100))
    widgetType = Column(SmallInteger)
    widgetFunction = Column(String(50), nullable=True)
    widgetHeading = Column(String(50), nullable=True)
    widgetContent = Column(String(3000), nullable=True)
    comments = Column(String(300), nullable=True)
    date_created = Column(DateTime, nullable=True)
    created_by = Column(String(100), nullable=True)

class WidgetsPlaced(Base):
    __tablename__ = "Widgets_Placed"
    widgetID = Column(Integer, primary_key=True)
    widgetType = Column(SmallInteger)
    depID = Column(Integer, nullable=True)
    area = Column(String(30))
    sortnum = Column(SmallInteger)

# -- AUTO GENERATED MODELS END

#— (paste any other stub‐models from stubs.txt here) —
