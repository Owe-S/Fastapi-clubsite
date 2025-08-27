<<<<<<< HEAD
from pydantic import BaseModel, Field
from typing import List, Optional, Any


class TableCell(BaseModel):
    tekst: Optional[str] = Field(None, example="Eksempel tekst")
    href: Optional[str] = Field(None, example="/path/to/resource")
    type: Optional[str] = Field(None, example="tekst")
    placeholder: Optional[str] = Field(None, example="Placeholder")
    funksjon: Optional[str] = Field(None, example="Vis/Slett")


class TableRow(BaseModel):
    celler: List[TableCell]


class TableModel(BaseModel):
    url: str = Field(..., example="https://skigk.no/csadmin/news")
    kolonner: List[str] = Field(..., example=["ID", "Tittel", "Forfatter"])
    rader: List[TableRow]


class MenuLink(BaseModel):
    navn: str = Field(..., example="Nyheter")
    url: str = Field(..., example="/admin/news")
    ikoner: Optional[List[str]] = Field(None, example=["icon-news"])
    underpunkter: Optional[List['MenuLink']] = None


MenuLink.update_forward_refs()


class PageModel(BaseModel):
    navn: str = Field(..., example="Nyheter")
    url: str = Field(..., example="/admin/news")
    beskrivelse: Optional[str] = Field(None, example="Beskrivelse av modulen")
    meny: List[MenuLink]
    tabeller: List[TableModel]

    model_config = {
        "json_schema_extra": {
            "example": {
                "navn": "Nyheter",
                "url": "/admin/news",
                "beskrivelse": "Modul for å publisere og administrere nyhetsartikler.",
                "meny": [{"navn": "Nyheter", "url": "/admin/news"}],
                "tabeller": [
                    {
                        "url": "https://skigk.no/csadmin/news",
                        "kolonner": ["ID", "Tittel", "Forfatter"],
                        "rader": [
                            {"celler": [{"tekst": "1", "type": "int"}, {"tekst": "Tittel..."}]}
                        ],
                    }
                ],
            }
        }
    }
=======
from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime, date

# --- Auth Schemas ---
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# --- News Schemas ---
class NewsIn(BaseModel):
    depID: int
    heading: str
    ingress: Optional[str] = None
    newscontent: Optional[str] = None
    validfrom: datetime
    validto: datetime
    boolPubl: bool
    author: Optional[str] = None
    template: Optional[int] = None
    videoUrl: Optional[str] = None

class NewsOut(BaseModel):
    articleID: int
    depID: int
    boolPubl: bool
    boolShow: bool
    boolPri: bool
    template: Optional[int]
    validfrom: datetime
    validto: datetime
    author: Optional[str]
    heading: str
    urlTitle: str
    indexImageID: Optional[int]
    indexImage: Optional[str]
    indexImagePath: Optional[str]
    indeximg_descr: Optional[str]
    templateImageID: Optional[int]
    templateImage: Optional[str]
    templimg_descr: Optional[str]
    ingress: Optional[str]
    newscontent: Optional[str]
    pagedescription: Optional[str]
    useFBcomments: Optional[bool]
    date_published: Optional[datetime]
    date_created: datetime
    created_by: Optional[str]
    date_modified: Optional[datetime]
    modified_by: Optional[str]
    amtReceivers: Optional[int]
    videoUrl: Optional[str]
    boolInfoscreen: Optional[bool]
    boolBoxed: Optional[bool]
    boolRss: Optional[bool]
    boolToFacebook: Optional[bool]

    class Config:
        from_attributes = True

# --- Activities Schemas ---
class ActivitiesBase(BaseModel):
    listID: int
    boolShow: bool
    activityName: str
    actAlias: Optional[str] = None
    location: Optional[str] = None
    maxParticipants: Optional[int] = None
    boolWaitlist: Optional[bool] = None
    partReserved: Optional[int] = None
    date_start: Optional[datetime] = None
    time_from: Optional[str] = None
    time_to: Optional[str] = None
    boolOnlinePay: bool
    boolOnlineSignup: bool
    formID: Optional[int] = None
    priceGroupID: Optional[int] = None
    signup_from: Optional[datetime] = None
    signup_to: Optional[datetime] = None
    actDescription: Optional[str] = None
    boolSignupToMail: Optional[bool] = None
    signupMailTo: Optional[str] = None
    boolVTG: Optional[bool] = None
    boolVTGforward: Optional[bool] = None
    payAccount: Optional[int] = None
    boolMemberRequired: Optional[bool] = None
    actLocation: Optional[str] = None
    field_borrowEquipment: Optional[bool] = None

class ActivitiesIn(ActivitiesBase):
    pass

class ActivitiesOut(ActivitiesBase):
    activityID: int
    date_created: datetime
    created_by: str
    date_modified: Optional[datetime] = None
    modified_by: Optional[str] = None

    class Config:
        from_attributes = True

# --- Activities_DateTime Schemas ---
class ActivitiesDateTimeBase(BaseModel):
    activityID: int
    actDate: date
    time_from: Optional[str] = None
    time_to: Optional[str] = None
    actDay: Optional[int] = None

class ActivitiesDateTimeIn(ActivitiesDateTimeBase):
    pass

class ActivitiesDateTimeOut(ActivitiesDateTimeBase):
    class Config:
        from_attributes = True

# --- News Schemas ---
from typing import Optional, List
from datetime import datetime

class NewsArticleBase(BaseModel):
    depID: int
    boolPubl: bool
    boolShow: bool
    boolPri: bool
    template: Optional[int] = None
    validfrom: datetime
    validto: datetime
    author: Optional[str] = None
    heading: str
    urlTitle: str
    indexImageID: Optional[int] = None
    indexImage: Optional[str] = None
    indexImagePath: Optional[str] = None
    indeximg_descr: Optional[str] = None
    templateImageID: Optional[int] = None
    templateImage: Optional[str] = None
    templimg_descr: Optional[str] = None
    ingress: Optional[str] = None
    newscontent: Optional[str] = None
    pagedescription: Optional[str] = None
    useFBcomments: Optional[bool] = None
    date_published: Optional[datetime] = None
    date_created: datetime
    created_by: str
    date_modified: Optional[datetime] = None
    modified_by: Optional[str] = None
    amtReceivers: Optional[int] = None
    videoUrl: Optional[str] = None
    boolInfoscreen: Optional[bool] = None
    boolBoxed: Optional[bool] = None
    boolRss: Optional[bool] = None
    boolToFacebook: Optional[bool] = None

class NewsArticleIn(NewsArticleBase):
    pass

class NewsArticleOut(NewsArticleBase):
    articleID: int

class NewsPluginBase(BaseModel):
    pluginID: int
    pluginRef: int

class NewsPluginOut(NewsPluginBase):
    articleID: int

class NewsBulletinBase(BaseModel):
    depID: int
    boolShow: bool
    heading: str
    urlTitle: str
    indexImageID: Optional[int] = None
    indexImage: Optional[str] = None
    indexImagePath: Optional[str] = None
    indeximg_descr: Optional[str] = None
    newscontent: Optional[str] = None
    pagedescription: Optional[str] = None

class NewsBulletinIn(NewsBulletinBase):
    pass

class NewsBulletinOut(NewsBulletinBase):
    articleID: int
    date_published: Optional[datetime] = None
    date_created: datetime
    created_by: str
    date_modified: Optional[datetime] = None
    modified_by: Optional[str] = None

class NewsKeywordBase(BaseModel):
    keyword: str
    numSearch: Optional[int] = None

class NewsKeywordOut(NewsKeywordBase):
    pass

from datetime import datetime
from typing import Optional

# --- Images Schemas ---
class ImageBase(BaseModel):
    depID: int
    categoryID: int
    imgWidth: Optional[int] = None
    imgHeight: Optional[int] = None
    imagename: str
    imagefile: str
    imgDescription: Optional[str] = None
    credits: Optional[str] = None
    sizecat: Optional[int] = None
    boolBoxed: Optional[bool] = None

class ImageIn(ImageBase):
    pass

class ImageOut(ImageBase):
    imageID: int
    date_created: datetime
    created_by: str

# Category schema
class ImageCategoryBase(BaseModel):
    depID: int
    category: str

class ImageCategoryIn(ImageCategoryBase):
    pass

class ImageCategoryOut(ImageCategoryBase):
    categoryID: int

# Courses
class CoursesBase(BaseModel):
    coursename: str
    urlTitle: Optional[str]
    holes: int
    sortnum: int
    boolShow: bool
    boolSlope: Optional[bool]

class CoursesIn(CoursesBase):
    pass

class CoursesOut(CoursesBase):
    courseID: int


# Course_Guide_Images
class CourseGuideImagesBase(BaseModel):
    hole: int
    courseID: int
    imagefile: Optional[str]
    imgDescription: Optional[str]
    sortnum: Optional[int]

class CourseGuideImagesIn(CourseGuideImagesBase):
    pass

class CourseGuideImagesOut(CourseGuideImagesBase):
    imageID: int


# Course_Guide_Sponsors
class CourseGuideSponsorsBase(BaseModel):
    courseID: Optional[int]
    hole: int

class CourseGuideSponsorsIn(CourseGuideSponsorsBase):
    pass

class CourseGuideSponsorsOut(CourseGuideSponsorsBase):
    sponsorID: int


# Course_Guide_Hole
class CourseGuideHoleBase(BaseModel):
    videourl: Optional[str]

class CourseGuideHoleIn(CourseGuideHoleBase):
    pass

class CourseGuideHoleOut(CourseGuideHoleBase):
    holeID: int


# Courses_Hio
class CoursesHioBase(BaseModel):
    pass

class CoursesHioIn(CoursesHioBase):
    pass

class CoursesHioOut(CoursesHioBase):
    hioID: int

# Alias singular→plural for dynamic router
class ImagesIn(ImageIn):
    """Matches model class Images"""
    pass

class ImagesOut(ImageOut):
    pass

class Images_CategoriesIn(ImageCategoryIn):
    """Matches model class Images_Categories"""
    pass

class Images_CategoriesOut(ImageCategoryOut):
    pass

# SiteUser schemas – needed so /siteuser shows up in docs
class SiteUserBase(BaseModel):
    """You can add real fields here later"""
    pass

class SiteUserIn(SiteUserBase):
    pass

class SiteUserOut(SiteUserBase):
    userID: int

from datetime import datetime

# --- AdminAreas Schemas ---
class AdminAreasBase(BaseModel):
    areaID: Optional[int]    = None
    area:   Optional[str]    = None

class AdminAreasIn(AdminAreasBase):
    pass

class AdminAreasOut(AdminAreasBase):
    areaID: int

# --- AdminUserPwdtemp Schemas ---
class AdminUserPwdtempBase(BaseModel):
    userID:    Optional[str]    = None
    pwdKey:    Optional[str]    = None
    pwdNumber: Optional[int]    = None
    timestamp: Optional[datetime] = None

class AdminUserPwdtempIn(AdminUserPwdtempBase):
    pass

class AdminUserPwdtempOut(AdminUserPwdtempBase):
    userID: str

# -- AUTO GENERATED SCHEMAS START
class ActivitiesParticipantsBase(BaseModel):
    participantID: Optional[int] = None
    activityID: Optional[int] = None
    boolSuConfirmed: Optional[int] = None
    orderID: Optional[int] = None
    price: Optional[int] = None
    pricecat: Optional[str] = None
    onWaitlist: Optional[int] = None
    parentname: Optional[str] = None
    fname: Optional[str] = None
    sname: Optional[str] = None
    email: Optional[str] = None
    memberID: Optional[str] = None
    bornyear: Optional[str] = None
    address: Optional[str] = None
    pcodecity: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    telephone: Optional[str] = None
    hcp: Optional[str] = None
    homeClub: Optional[str] = None
    comments: Optional[str] = None
    extraInfo: Optional[str] = None
    date_signup: Optional[int] = None
    signupKey: Optional[str] = None
    vtgMembership: Optional[int] = None
    memberByVtg: Optional[int] = None
    parentemail: Optional[str] = None
    parentphone: Optional[str] = None
    boolDeleted: Optional[int] = None
class ActivitiesParticipantsIn(ActivitiesParticipantsBase):
    pass
class ActivitiesParticipantsOut(ActivitiesParticipantsBase):
    participantID: int

class ActivitiesPricegroupPricesBase(BaseModel):
    priceCatID: Optional[int] = None
    groupID: Optional[int] = None
    pricecatname: Optional[str] = None
    price: Optional[int] = None
class ActivitiesPricegroupPricesIn(ActivitiesPricegroupPricesBase):
    pass
class ActivitiesPricegroupPricesOut(ActivitiesPricegroupPricesBase):
    priceCatID: int

class ActivitiesPricegroupsBase(BaseModel):
    groupID: Optional[int] = None
    depID: Optional[int] = None
    actType: Optional[str] = None
    priceGroup: Optional[str] = None
    boolActive: Optional[int] = None
class ActivitiesPricegroupsIn(ActivitiesPricegroupsBase):
    pass
class ActivitiesPricegroupsOut(ActivitiesPricegroupsBase):
    groupID: int

class ActivitiesPricesBase(BaseModel):
    priceID: Optional[int] = None
    activityID: Optional[int] = None
    tournID: Optional[int] = None
    pricecat: Optional[str] = None
    price: Optional[int] = None
class ActivitiesPricesIn(ActivitiesPricesBase):
    pass
class ActivitiesPricesOut(ActivitiesPricesBase):
    priceID: int

class AdminUsersBase(BaseModel):
    userID: Optional[int] = None
    boolSupervisor: Optional[int] = None
    adminName: Optional[str] = None
    adminEmail: Optional[str] = None
    pwd_hash: Optional[str] = None
    pwd_temp: Optional[str] = None
    date_created: Optional[int] = None
    lastLog: Optional[int] = None
    cKey: Optional[str] = None
class AdminUsersIn(AdminUsersBase):
    pass
class AdminUsersOut(AdminUsersBase):
    userID: int

class AdminUsersAreasBase(BaseModel):
    areaID: Optional[int] = None
    userID: Optional[int] = None
class AdminUsersAreasIn(AdminUsersAreasBase):
    pass
class AdminUsersAreasOut(AdminUsersAreasBase):
    areaID: int

class AdminUsersDepartmentsBase(BaseModel):
    userID: Optional[int] = None
    depID: Optional[int] = None
    preferred: Optional[int] = None
class AdminUsersDepartmentsIn(AdminUsersDepartmentsBase):
    pass
class AdminUsersDepartmentsOut(AdminUsersDepartmentsBase):
    userID: int

class AdsBase(BaseModel):
    adID: Optional[int] = None
    boolShow: Optional[int] = None
    catID: Optional[int] = None
    contact: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    price: Optional[str] = None
    date_created: Optional[int] = None
class AdsIn(AdsBase):
    pass
class AdsOut(AdsBase):
    adID: int

class AdsCategoriesBase(BaseModel):
    catID: Optional[int] = None
    category: Optional[str] = None
class AdsCategoriesIn(AdsCategoriesBase):
    pass
class AdsCategoriesOut(AdsCategoriesBase):
    catID: int

class AttachmentsBase(BaseModel):
    attachmentID: Optional[int] = None
    documentID: Optional[int] = None
    pageID: Optional[int] = None
    articleID: Optional[int] = None
    tournID: Optional[int] = None
    activityID: Optional[int] = None
    safeField: Optional[int] = None
class AttachmentsIn(AttachmentsBase):
    pass
class AttachmentsOut(AttachmentsBase):
    attachmentID: int

class BlogBase(BaseModel):
    blogID: Optional[int] = None
    bloggerID: Optional[int] = None
    boolShow: Optional[int] = None
    typeComments: Optional[str] = None
    pagedescription: Optional[str] = None
    template: Optional[int] = None
    indexImageID: Optional[int] = None
    indexImage: Optional[str] = None
    indexImagePath: Optional[str] = None
    indeximg_descr: Optional[str] = None
    templateImageID: Optional[int] = None
    templateImage: Optional[str] = None
    templimg_descr: Optional[str] = None
    validfrom: Optional[int] = None
    heading: Optional[str] = None
    urlTitle: Optional[str] = None
    blogContent: Optional[str] = None
    boolSendNotice: Optional[int] = None
    noticeToEmail: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    videoUrl: Optional[str] = None
class BlogIn(BlogBase):
    pass
class BlogOut(BlogBase):
    blogID: int

class BlogCommentsBase(BaseModel):
    commentID: Optional[int] = None
    blogID: Optional[int] = None
    comment: Optional[str] = None
    boolShow: Optional[int] = None
    poster: Optional[str] = None
    poster_email: Optional[str] = None
    date_created: Optional[int] = None
    admin_comment: Optional[str] = None
    bloggerID: Optional[int] = None
    date_reply: Optional[int] = None
class BlogCommentsIn(BlogCommentsBase):
    pass
class BlogCommentsOut(BlogCommentsBase):
    commentID: int

class BlogImagesBase(BaseModel):
    imageID: Optional[int] = None
    bloggerID: Optional[int] = None
    imgWidth: Optional[str] = None
    imgHeight: Optional[str] = None
    imagefile: Optional[str] = None
    imgDescription: Optional[str] = None
    sizecat: Optional[int] = None
    date_created: Optional[int] = None
class BlogImagesIn(BlogImagesBase):
    pass
class BlogImagesOut(BlogImagesBase):
    imageID: int

class BloggersBase(BaseModel):
    bloggerID: Optional[int] = None
    boolShow: Optional[int] = None
    bloggerName: Optional[str] = None
    bloggerAlias: Optional[str] = None
    bloggerLogin: Optional[str] = None
    bloggerEmail: Optional[str] = None
    pwdHash: Optional[str] = None
    ckey: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class BloggersIn(BloggersBase):
    pass
class BloggersOut(BloggersBase):
    bloggerID: int

class CalendarBase(BaseModel):
    calID: Optional[int] = None
    depID: Optional[int] = None
    descr: Optional[str] = None
    tournID: Optional[int] = None
    activityID: Optional[int] = None
    calDate: Optional[int] = None
    timeFrom: Optional[str] = None
    timeTo: Optional[str] = None
    details: Optional[str] = None
class CalendarIn(CalendarBase):
    pass
class CalendarOut(CalendarBase):
    calID: int

class CartBase(BaseModel):
    cartRowID: Optional[int] = None
    cartID: Optional[str] = None
    noProd: Optional[int] = None
    productID: Optional[int] = None
    prodVarID: Optional[int] = None
    activityID: Optional[int] = None
    tournID: Optional[int] = None
    feedbackID: Optional[int] = None
    senderID: Optional[int] = None
    participantID: Optional[int] = None
    variant: Optional[str] = None
    textVariant: Optional[str] = None
    totPrice: Optional[int] = None
    quantity: Optional[int] = None
    totalValue: Optional[int] = None
    dateAdded: Optional[int] = None
    ip: Optional[str] = None
    memberRecID: Optional[int] = None
    payAccount: Optional[int] = None
class CartIn(CartBase):
    pass
class CartOut(CartBase):
    cartRowID: int

class ClubchampsBase(BaseModel):
    championID: Optional[int] = None
    ch_year: Optional[str] = None
    categoryID: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    rounds: Optional[str] = None
    score: Optional[str] = None
    imagepath: Optional[str] = None
    tee: Optional[str] = None
    url_res: Optional[str] = None
class ClubchampsIn(ClubchampsBase):
    pass
class ClubchampsOut(ClubchampsBase):
    championID: int

class ClubchampsCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    category: Optional[str] = None
    sortnum: Optional[int] = None
    tee: Optional[str] = None
class ClubchampsCategoriesIn(ClubchampsCategoriesBase):
    pass
class ClubchampsCategoriesOut(ClubchampsCategoriesBase):
    categoryID: int

class ContactsBase(BaseModel):
    contactID: Optional[int] = None
    listID: Optional[int] = None
    profileID: Optional[int] = None
    sortnum: Optional[int] = None
    contactTitle: Optional[str] = None
class ContactsIn(ContactsBase):
    pass
class ContactsOut(ContactsBase):
    contactID: int

class ContactsListBase(BaseModel):
    listID: Optional[int] = None
    depID: Optional[int] = None
    listname: Optional[str] = None
    listtype: Optional[str] = None
    sortnum: Optional[int] = None
    boolShow: Optional[int] = None
    useDescription: Optional[int] = None
    useIcons: Optional[int] = None
class ContactsListIn(ContactsListBase):
    pass
class ContactsListOut(ContactsListBase):
    listID: int

class CoursesParBase(BaseModel):
    courseID: Optional[int] = None
    p1: Optional[int] = None
    p2: Optional[int] = None
    p3: Optional[int] = None
    p4: Optional[int] = None
    p5: Optional[int] = None
    p6: Optional[int] = None
    p7: Optional[int] = None
    p8: Optional[int] = None
    p9: Optional[int] = None
    p10: Optional[int] = None
    p11: Optional[int] = None
    p12: Optional[int] = None
    p13: Optional[int] = None
    p14: Optional[int] = None
    p15: Optional[int] = None
    p16: Optional[int] = None
    p17: Optional[int] = None
    p18: Optional[int] = None
    pfront: Optional[int] = None
    pback: Optional[int] = None
    par: Optional[int] = None
    i1: Optional[int] = None
    i2: Optional[int] = None
    i3: Optional[int] = None
    i4: Optional[int] = None
    i5: Optional[int] = None
    i6: Optional[int] = None
    i7: Optional[int] = None
    i8: Optional[int] = None
    i9: Optional[int] = None
    i10: Optional[int] = None
    i11: Optional[int] = None
    i12: Optional[int] = None
    i13: Optional[int] = None
    i14: Optional[int] = None
    i15: Optional[int] = None
    i16: Optional[int] = None
    i17: Optional[int] = None
    i18: Optional[int] = None
    n1: Optional[str] = None
    n2: Optional[str] = None
    n3: Optional[str] = None
    n4: Optional[str] = None
    n5: Optional[str] = None
    n6: Optional[str] = None
    n7: Optional[str] = None
    n8: Optional[str] = None
    n9: Optional[str] = None
    n10: Optional[str] = None
    n11: Optional[str] = None
    n12: Optional[str] = None
    n13: Optional[str] = None
    n14: Optional[str] = None
    n15: Optional[str] = None
    n16: Optional[str] = None
    n17: Optional[str] = None
    n18: Optional[str] = None
class CoursesParIn(CoursesParBase):
    pass
class CoursesParOut(CoursesParBase):
    courseID: int

class CoursesTeesBase(BaseModel):
    teeID: Optional[int] = None
    courseID: Optional[int] = None
    sortnum: Optional[int] = None
    teename: Optional[str] = None
    cr_m: Optional[int] = None
    cr_f: Optional[int] = None
    slope_m: Optional[int] = None
    slope_f: Optional[int] = None
    l1: Optional[str] = None
    l2: Optional[str] = None
    l3: Optional[str] = None
    l4: Optional[str] = None
    l5: Optional[str] = None
    l6: Optional[str] = None
    l7: Optional[str] = None
    l8: Optional[str] = None
    l9: Optional[str] = None
    l10: Optional[str] = None
    l11: Optional[str] = None
    l12: Optional[str] = None
    l13: Optional[str] = None
    l14: Optional[str] = None
    l15: Optional[str] = None
    l16: Optional[str] = None
    l17: Optional[str] = None
    l18: Optional[str] = None
    lf9: Optional[str] = None
    lb9: Optional[str] = None
    ltotal: Optional[str] = None
class CoursesTeesIn(CoursesTeesBase):
    pass
class CoursesTeesOut(CoursesTeesBase):
    teeID: int

class DepartmentsBase(BaseModel):
    depID: Optional[int] = None
    boolShow: Optional[int] = None
    boolMainDep: Optional[int] = None
    department: Optional[str] = None
    urlAlias: Optional[str] = None
    slogan: Optional[str] = None
    megasort: Optional[int] = None
    date_created: Optional[int] = None
    boolRequired: Optional[int] = None
    boolMemberArea: Optional[int] = None
    boolModuleDirect: Optional[int] = None
class DepartmentsIn(DepartmentsBase):
    pass
class DepartmentsOut(DepartmentsBase):
    depID: int

class DocumentsBase(BaseModel):
    documentID: Optional[int] = None
    oldDokID: Optional[int] = None
    depID: Optional[int] = None
    boolShow: Optional[int] = None
    categoryID: Optional[int] = None
    docname: Optional[str] = None
    docdescription: Optional[str] = None
    docformat: Optional[str] = None
    docfile: Optional[str] = None
    size: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    created_by: Optional[str] = None
class DocumentsIn(DocumentsBase):
    pass
class DocumentsOut(DocumentsBase):
    documentID: int

class DocumentsCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    parentID: Optional[int] = None
    depID: Optional[int] = None
    category: Optional[str] = None
    start: Optional[int] = None
class DocumentsCategoriesIn(DocumentsCategoriesBase):
    pass
class DocumentsCategoriesOut(DocumentsCategoriesBase):
    categoryID: int

class DocumentsUserregBase(BaseModel):
    documentID: Optional[int] = None
    boolShow: Optional[int] = None
    categoryID: Optional[int] = None
    docname: Optional[str] = None
    docdescription: Optional[str] = None
    docformat: Optional[str] = None
    docfile: Optional[str] = None
    size: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    created_by: Optional[str] = None
class DocumentsUserregIn(DocumentsUserregBase):
    pass
class DocumentsUserregOut(DocumentsUserregBase):
    documentID: int

class DocumentsUserregCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    category: Optional[str] = None
class DocumentsUserregCategoriesIn(DocumentsUserregCategoriesBase):
    pass
class DocumentsUserregCategoriesOut(DocumentsUserregCategoriesBase):
    categoryID: int

class EclecticCoursesBase(BaseModel):
    ecl_tournID: Optional[int] = None
    coursename: Optional[str] = None
    p1: Optional[int] = None
    p2: Optional[int] = None
    p3: Optional[int] = None
    p4: Optional[int] = None
    p5: Optional[int] = None
    p6: Optional[int] = None
    p7: Optional[int] = None
    p8: Optional[int] = None
    p9: Optional[int] = None
    p10: Optional[int] = None
    p11: Optional[int] = None
    p12: Optional[int] = None
    p13: Optional[int] = None
    p14: Optional[int] = None
    p15: Optional[int] = None
    p16: Optional[int] = None
    p17: Optional[int] = None
    p18: Optional[int] = None
    pfront: Optional[int] = None
    pback: Optional[int] = None
    par: Optional[int] = None
    i1: Optional[int] = None
    i2: Optional[int] = None
    i3: Optional[int] = None
    i4: Optional[int] = None
    i5: Optional[int] = None
    i6: Optional[int] = None
    i7: Optional[int] = None
    i8: Optional[int] = None
    i9: Optional[int] = None
    i10: Optional[int] = None
    i11: Optional[int] = None
    i12: Optional[int] = None
    i13: Optional[int] = None
    i14: Optional[int] = None
    i15: Optional[int] = None
    i16: Optional[int] = None
    i17: Optional[int] = None
    i18: Optional[int] = None
class EclecticCoursesIn(EclecticCoursesBase):
    pass
class EclecticCoursesOut(EclecticCoursesBase):
    ecl_tournID: int

class EclecticParticipantsBase(BaseModel):
    participantID: Optional[int] = None
    oldID: Optional[int] = None
    ecl_TournID: Optional[int] = None
    fname: Optional[str] = None
    lname: Optional[str] = None
    hcp: Optional[str] = None
class EclecticParticipantsIn(EclecticParticipantsBase):
    pass
class EclecticParticipantsOut(EclecticParticipantsBase):
    participantID: int

class EclecticScoreBase(BaseModel):
    scoreID: Optional[int] = None
    ecl_tournID: Optional[int] = None
    participantID: Optional[int] = None
    hcp: Optional[str] = None
    MS: Optional[int] = None
    scoreDate: Optional[int] = None
    sc1: Optional[str] = None
    sc2: Optional[str] = None
    sc3: Optional[str] = None
    sc4: Optional[str] = None
    sc5: Optional[str] = None
    sc6: Optional[str] = None
    sc7: Optional[str] = None
    sc8: Optional[str] = None
    sc9: Optional[str] = None
    sc10: Optional[str] = None
    sc11: Optional[str] = None
    sc12: Optional[str] = None
    sc13: Optional[str] = None
    sc14: Optional[str] = None
    sc15: Optional[str] = None
    sc16: Optional[str] = None
    sc17: Optional[str] = None
    sc18: Optional[str] = None
    sumScore: Optional[str] = None
    sumAlb: Optional[str] = None
    sumEag: Optional[str] = None
    sumBir: Optional[str] = None
    sumPar: Optional[str] = None
    sumBog: Optional[str] = None
    sumDbo: Optional[str] = None
    sumOth: Optional[str] = None
class EclecticScoreIn(EclecticScoreBase):
    pass
class EclecticScoreOut(EclecticScoreBase):
    scoreID: int

class EclecticScoreNetBase(BaseModel):
    scoreID: Optional[int] = None
    ecl_tournID: Optional[int] = None
    participantID: Optional[int] = None
    sc1: Optional[str] = None
    sc2: Optional[str] = None
    sc3: Optional[str] = None
    sc4: Optional[str] = None
    sc5: Optional[str] = None
    sc6: Optional[str] = None
    sc7: Optional[str] = None
    sc8: Optional[str] = None
    sc9: Optional[str] = None
    sc10: Optional[str] = None
    sc11: Optional[str] = None
    sc12: Optional[str] = None
    sc13: Optional[str] = None
    sc14: Optional[str] = None
    sc15: Optional[str] = None
    sc16: Optional[str] = None
    sc17: Optional[str] = None
    sc18: Optional[str] = None
    sumScore: Optional[str] = None
class EclecticScoreNetIn(EclecticScoreNetBase):
    pass
class EclecticScoreNetOut(EclecticScoreNetBase):
    scoreID: int

class EclecticScoreStblBase(BaseModel):
    scoreID: Optional[int] = None
    participantID: Optional[int] = None
    ecl_tournID: Optional[int] = None
    sc1: Optional[str] = None
    sc2: Optional[str] = None
    sc3: Optional[str] = None
    sc4: Optional[str] = None
    sc5: Optional[str] = None
    sc6: Optional[str] = None
    sc7: Optional[str] = None
    sc8: Optional[str] = None
    sc9: Optional[str] = None
    sc10: Optional[str] = None
    sc11: Optional[str] = None
    sc12: Optional[str] = None
    sc13: Optional[str] = None
    sc14: Optional[str] = None
    sc15: Optional[str] = None
    sc16: Optional[str] = None
    sc17: Optional[str] = None
    sc18: Optional[str] = None
    sumScore: Optional[str] = None
class EclecticScoreStblIn(EclecticScoreStblBase):
    pass
class EclecticScoreStblOut(EclecticScoreStblBase):
    scoreID: int

class EclecticTournamentsBase(BaseModel):
    ecl_tournID: Optional[int] = None
    depID: Optional[int] = None
    boolShow: Optional[int] = None
    holes: Optional[str] = None
    tournName: Optional[str] = None
    eclAlias: Optional[str] = None
    tournInfo: Optional[str] = None
    tournType: Optional[int] = None
    rangType: Optional[int] = None
    sortnum: Optional[int] = None
class EclecticTournamentsIn(EclecticTournamentsBase):
    pass
class EclecticTournamentsOut(EclecticTournamentsBase):
    ecl_tournID: int

class ElementsDatesliderBase(BaseModel):
    img_mon: Optional[str] = None
    img_tue: Optional[str] = None
    img_wed: Optional[str] = None
    img_thu: Optional[str] = None
    img_fri: Optional[str] = None
    img_sat: Optional[str] = None
    img_sun: Optional[str] = None
    useStaticContent: Optional[int] = None
    staticContent: Optional[str] = None
    sliderbox_useicon: Optional[int] = None
class ElementsDatesliderIn(ElementsDatesliderBase):
    pass
class ElementsDatesliderOut(ElementsDatesliderBase):
    img_mon: int

class ElementsDatesliderDatesBase(BaseModel):
    img_date: Optional[int] = None
    img_file: Optional[str] = None
class ElementsDatesliderDatesIn(ElementsDatesliderDatesBase):
    pass
class ElementsDatesliderDatesOut(ElementsDatesliderDatesBase):
    img_date: int

class ElementsDatesliderSlidesBase(BaseModel):
    slideID: Optional[int] = None
    boolShow: Optional[int] = None
    align_vert: Optional[str] = None
    align_hor: Optional[str] = None
    lineBig: Optional[str] = None
    lineSmall: Optional[str] = None
    button_1_text: Optional[str] = None
    button_1_url: Optional[str] = None
    button_2_text: Optional[str] = None
    button_2_url: Optional[str] = None
    sortnum: Optional[int] = None
    button_3_text: Optional[str] = None
    button_3_url: Optional[str] = None
    button_1_url_ext: Optional[int] = None
    button_2_url_ext: Optional[int] = None
    button_3_url_ext: Optional[int] = None
    button_4_text: Optional[str] = None
    button_4_url: Optional[str] = None
    button_4_url_ext: Optional[int] = None
class ElementsDatesliderSlidesIn(ElementsDatesliderSlidesBase):
    pass
class ElementsDatesliderSlidesOut(ElementsDatesliderSlidesBase):
    slideID: int

class ElementsFlexsliderElementsBase(BaseModel):
    elementID: Optional[int] = None
    sliderID: Optional[int] = None
    boolShow: Optional[int] = None
    elName: Optional[str] = None
    elImagefile: Optional[str] = None
    elUrl: Optional[str] = None
    elCaption: Optional[str] = None
    sortnum: Optional[int] = None
class ElementsFlexsliderElementsIn(ElementsFlexsliderElementsBase):
    pass
class ElementsFlexsliderElementsOut(ElementsFlexsliderElementsBase):
    elementID: int

class ElementsFlexsliderSlidersBase(BaseModel):
    sliderID: Optional[int] = None
    boolShow: Optional[int] = None
    slidername: Optional[str] = None
    comments: Optional[str] = None
    height: Optional[str] = None
    boolFullwidth: Optional[int] = None
    boolTwothird: Optional[int] = None
    boolOnethird: Optional[int] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class ElementsFlexsliderSlidersIn(ElementsFlexsliderSlidersBase):
    pass
class ElementsFlexsliderSlidersOut(ElementsFlexsliderSlidersBase):
    sliderID: int

class ElementsLayersliderLayersBase(BaseModel):
    layerID: Optional[int] = None
    slideID: Optional[int] = None
    pauseIn: Optional[str] = None
    distTop: Optional[str] = None
    distLeft: Optional[str] = None
    animIn: Optional[str] = None
    animOut: Optional[str] = None
    textAlign: Optional[str] = None
    lineBig: Optional[str] = None
    lineSmall: Optional[str] = None
    button_1_text: Optional[str] = None
    button_1_url: Optional[str] = None
    button_2_text: Optional[str] = None
    button_2_url: Optional[str] = None
class ElementsLayersliderLayersIn(ElementsLayersliderLayersBase):
    pass
class ElementsLayersliderLayersOut(ElementsLayersliderLayersBase):
    layerID: int

class ElementsLayersliderSlidesBase(BaseModel):
    slideID: Optional[int] = None
    parentID: Optional[int] = None
    sortnum: Optional[int] = None
    boolShow: Optional[int] = None
    slide_name: Optional[str] = None
    slide_delay: Optional[str] = None
    slide_transition: Optional[str] = None
    bg_image: Optional[str] = None
class ElementsLayersliderSlidesIn(ElementsLayersliderSlidesBase):
    pass
class ElementsLayersliderSlidesOut(ElementsLayersliderSlidesBase):
    slideID: int

class FaqBase(BaseModel):
    qID: Optional[int] = None
    categoryID: Optional[int] = None
    boolShow: Optional[int] = None
    question: Optional[str] = None
    answer: Optional[str] = None
    sortnum: Optional[int] = None
    depID: Optional[int] = None
class FaqIn(FaqBase):
    pass
class FaqOut(FaqBase):
    qID: int

class FaqCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    category: Optional[str] = None
    boolShow: Optional[int] = None
    sortnum: Optional[int] = None
    depID: Optional[int] = None
class FaqCategoriesIn(FaqCategoriesBase):
    pass
class FaqCategoriesOut(FaqCategoriesBase):
    categoryID: int

class FeedbacksBase(BaseModel):
    feedbackID: Optional[int] = None
    depID: Optional[int] = None
    feedbackName: Optional[str] = None
    activefrom: Optional[int] = None
    activeto: Optional[int] = None
    formID: Optional[int] = None
    priceGroupID: Optional[int] = None
    boolFormToMail: Optional[int] = None
    admMailTo: Optional[str] = None
    boolOnlinePay: Optional[int] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class FeedbacksIn(FeedbacksBase):
    pass
class FeedbacksOut(FeedbacksBase):
    feedbackID: int

class FeedbacksInBase(BaseModel):
    senderID: Optional[int] = None
    feedbackID: Optional[int] = None
    boolSuConfirmed: Optional[int] = None
    orderID: Optional[int] = None
    price: Optional[int] = None
    pricecat: Optional[str] = None
    parentinfo: Optional[str] = None
    fname: Optional[str] = None
    lname: Optional[str] = None
    fullname: Optional[str] = None
    email: Optional[str] = None
    memberID: Optional[str] = None
    bornyear: Optional[str] = None
    address: Optional[str] = None
    pcodecity: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    telephone: Optional[str] = None
    hcp: Optional[str] = None
    seldate: Optional[int] = None
    homeClub: Optional[str] = None
    comments: Optional[str] = None
    extraInfo: Optional[str] = None
    date_created: Optional[int] = None
class FeedbacksInIn(FeedbacksInBase):
    pass
class FeedbacksInOut(FeedbacksInBase):
    senderID: int

class FormsBase(BaseModel):
    formID: Optional[int] = None
    depID: Optional[int] = None
    formName: Optional[str] = None
    formType: Optional[str] = None
    formDescription: Optional[str] = None
    mailReceiver: Optional[str] = None
    date_created: Optional[int] = None
    date_updated: Optional[int] = None
    created_by: Optional[str] = None
class FormsIn(FormsBase):
    pass
class FormsOut(FormsBase):
    formID: int

class FormsBymailBase(BaseModel):
    recID: Optional[int] = None
    formID: Optional[int] = None
    formname: Optional[str] = None
    maildate: Optional[int] = None
    tomail: Optional[str] = None
    fromname: Optional[str] = None
    fromemail: Optional[str] = None
    theForm: Optional[str] = None
    formkey: Optional[str] = None
class FormsBymailIn(FormsBymailBase):
    pass
class FormsBymailOut(FormsBymailBase):
    recID: int

class FormsFieldsBase(BaseModel):
    formID: Optional[int] = None
    fieldID: Optional[int] = None
    required: Optional[int] = None
    sortnum: Optional[int] = None
class FormsFieldsIn(FormsFieldsBase):
    pass
class FormsFieldsOut(FormsFieldsBase):
    formID: int

class FormsFieldsOptionsBase(BaseModel):
    optionID: Optional[int] = None
    fieldID: Optional[int] = None
    selOption: Optional[str] = None
    sortnum: Optional[int] = None
class FormsFieldsOptionsIn(FormsFieldsOptionsBase):
    pass
class FormsFieldsOptionsOut(FormsFieldsOptionsBase):
    optionID: int

class FormsFieldsSourceBase(BaseModel):
    fieldID: Optional[int] = None
    depID: Optional[int] = None
    predef: Optional[int] = None
    fieldname: Optional[str] = None
    fieldlabel: Optional[str] = None
    fieldTypeID: Optional[int] = None
    fieldDescr: Optional[str] = None
    maxchars: Optional[int] = None
    fieldwidth: Optional[str] = None
    arearows: Optional[int] = None
class FormsFieldsSourceIn(FormsFieldsSourceBase):
    pass
class FormsFieldsSourceOut(FormsFieldsSourceBase):
    fieldID: int

class FormsFieldtypesBase(BaseModel):
    fieldTypeID: Optional[int] = None
    fieldType: Optional[str] = None
    preDef: Optional[int] = None
    descr: Optional[str] = None
    sort: Optional[int] = None
    boolShow: Optional[int] = None
    defFunction: Optional[str] = None
class FormsFieldtypesIn(FormsFieldtypesBase):
    pass
class FormsFieldtypesOut(FormsFieldtypesBase):
    fieldTypeID: int

class FormsReceivedBase(BaseModel):
    recID: Optional[int] = None
    form: Optional[str] = None
    sender_lname: Optional[str] = None
    sender_fname: Optional[str] = None
    sender_email: Optional[str] = None
    to_mail: Optional[str] = None
    formContent: Optional[str] = None
    formKey: Optional[str] = None
    date_created: Optional[int] = None
class FormsReceivedIn(FormsReceivedBase):
    pass
class FormsReceivedOut(FormsReceivedBase):
    recID: int

class FormsTypesBase(BaseModel):
    formType: Optional[int] = None
    typename: Optional[str] = None
class FormsTypesIn(FormsTypesBase):
    pass
class FormsTypesOut(FormsTypesBase):
    formType: int

class ImagesCcondBase(BaseModel):
    imageID: Optional[int] = None
    imagefile: Optional[str] = None
    date_created: Optional[int] = None
class ImagesCcondIn(ImagesCcondBase):
    pass
class ImagesCcondOut(ImagesCcondBase):
    imageID: int

class ImagesProfilesBase(BaseModel):
    imageID: Optional[int] = None
    imagepath: Optional[str] = None
    imagefile: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    date_created: Optional[int] = None
class ImagesProfilesIn(ImagesProfilesBase):
    pass
class ImagesProfilesOut(ImagesProfilesBase):
    imageID: int

class ImagesSliderBase(BaseModel):
    imageID: Optional[int] = None
    imagefile: Optional[str] = None
    date_created: Optional[int] = None
    depID: Optional[int] = None
class ImagesSliderIn(ImagesSliderBase):
    pass
class ImagesSliderOut(ImagesSliderBase):
    imageID: int

class MembersChangeBase(BaseModel):
    recID: Optional[int] = None
    membernum: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    memberemail: Optional[str] = None
    cat_old: Optional[str] = None
    cat_new: Optional[str] = None
    comments: Optional[str] = None
    formkey: Optional[str] = None
    terms: Optional[str] = None
    terms_extra: Optional[str] = None
    boolDeleted: Optional[int] = None
    date_created: Optional[int] = None
    famMembers: Optional[str] = None
class MembersChangeIn(MembersChangeBase):
    pass
class MembersChangeOut(MembersChangeBase):
    recID: int

class MembersInBase(BaseModel):
    recID: Optional[int] = None
    orderID: Optional[int] = None
    orderConfirmed: Optional[int] = None
    born: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    membAddress: Optional[str] = None
    pcodecity: Optional[str] = None
    fromEmail: Optional[str] = None
    phone: Optional[str] = None
    parentname: Optional[str] = None
    parentphone: Optional[str] = None
    parentemail: Optional[str] = None
    hcp: Optional[str] = None
    membOtherClub: Optional[str] = None
    otherClubname: Optional[str] = None
    boolHomeclub: Optional[str] = None
    boolEcoDue: Optional[str] = None
    houseMagazine: Optional[str] = None
    wishMagazine: Optional[str] = None
    membercat: Optional[str] = None
    familyRelations: Optional[str] = None
    extra_1: Optional[str] = None
    extra_2: Optional[str] = None
    extra_3: Optional[str] = None
    comments: Optional[str] = None
    formkey: Optional[str] = None
    date_created: Optional[int] = None
    boolDeleted: Optional[int] = None
    terms: Optional[str] = None
    payPeriode: Optional[str] = None
    terms_extra: Optional[str] = None
    vtgCourse: Optional[str] = None
    vtgClub: Optional[str] = None
    gender: Optional[str] = None
    vtgYear: Optional[str] = None
    otherMembernum: Optional[str] = None
    boolAdult: Optional[int] = None
    vtgID: Optional[int] = None
    categoryID: Optional[int] = None
    otherClubMemberNum: Optional[str] = None
    familyMembership: Optional[int] = None
    customerclub: Optional[str] = None
    participantID_vtg: Optional[int] = None
    borndate: Optional[int] = None
    junOrgTraining: Optional[str] = None
class MembersInIn(MembersInBase):
    pass
class MembersInOut(MembersInBase):
    recID: int

class MembersOutBase(BaseModel):
    recID: Optional[int] = None
    membernum: Optional[str] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    comments: Optional[str] = None
    formkey: Optional[str] = None
    contactMe: Optional[str] = None
    date_created: Optional[int] = None
    boolDeleted: Optional[int] = None
    reason: Optional[str] = None
    supportMember: Optional[str] = None
class MembersOutIn(MembersOutBase):
    pass
class MembersOutOut(MembersOutBase):
    recID: int

class MembersSignoutSourceBase(BaseModel):
    fieldID: Optional[int] = None
    fieldname: Optional[str] = None
    fieldtype: Optional[int] = None
    fieldExplain: Optional[str] = None
    boolShow: Optional[int] = None
    boolActive: Optional[int] = None
    db_col: Optional[str] = None
    field_html: Optional[str] = None
    sortnum: Optional[int] = None
class MembersSignoutSourceIn(MembersSignoutSourceBase):
    pass
class MembersSignoutSourceOut(MembersSignoutSourceBase):
    fieldID: int

class MembersSignupSourceBase(BaseModel):
    fieldID: Optional[int] = None
    fieldname: Optional[str] = None
    fieldtype: Optional[int] = None
    fieldExplain: Optional[str] = None
    boolShow: Optional[int] = None
    boolActive: Optional[int] = None
    db_col: Optional[str] = None
    field_html: Optional[str] = None
    sortnum: Optional[int] = None
class MembersSignupSourceIn(MembersSignupSourceBase):
    pass
class MembersSignupSourceOut(MembersSignupSourceBase):
    fieldID: int

class MembershipsBase(BaseModel):
    categoryID: Optional[int] = None
    boolShow: Optional[int] = None
    category: Optional[str] = None
    sortnum: Optional[int] = None
    catprice: Optional[int] = None
    price_quota: Optional[str] = None
    catdescription: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    boolTerms: Optional[int] = None
    catterms: Optional[str] = None
    boolFamily: Optional[int] = None
    catmail: Optional[str] = None
    boolCatmail: Optional[int] = None
    catprice_month: Optional[int] = None
    catprice_year: Optional[int] = None
    show_priceMonth: Optional[int] = None
    show_priceYear: Optional[int] = None
    boolSelInVtg: Optional[int] = None
    boolSelectSignup: Optional[int] = None
    boolSelectChangecat: Optional[int] = None
class MembershipsIn(MembershipsBase):
    pass
class MembershipsOut(MembershipsBase):
    categoryID: int

class MembershipsVtgBase(BaseModel):
    vtgListID: Optional[int] = None
    membercatID: Optional[int] = None
class MembershipsVtgIn(MembershipsVtgBase):
    pass
class MembershipsVtgOut(MembershipsVtgBase):
    vtgListID: int

class MenuMainBase(BaseModel):
    itemID: Optional[int] = None
    parentID: Optional[int] = None
    boolShow: Optional[int] = None
    boolNewWin: Optional[int] = None
    sortnum: Optional[int] = None
    item: Optional[str] = None
    itemlink: Optional[str] = None
    icon: Optional[str] = None
class MenuMainIn(MenuMainBase):
    pass
class MenuMainOut(MenuMainBase):
    itemID: int

class NewsArticlesPluginsBase(BaseModel):
    articleID: Optional[int] = None
    pluginID: Optional[int] = None
    pluginRef: Optional[int] = None
class NewsArticlesPluginsIn(NewsArticlesPluginsBase):
    pass
class NewsArticlesPluginsOut(NewsArticlesPluginsBase):
    articleID: int

class NewsBulletinsBase(BaseModel):
    articleID: Optional[int] = None
    depID: Optional[int] = None
    boolShow: Optional[int] = None
    heading: Optional[str] = None
    urlTitle: Optional[str] = None
    indexImageID: Optional[int] = None
    indexImage: Optional[str] = None
    indexImagePath: Optional[str] = None
    indeximg_descr: Optional[str] = None
    newscontent: Optional[str] = None
    pagedescription: Optional[str] = None
    date_published: Optional[int] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    date_modified: Optional[int] = None
    modified_by: Optional[str] = None
class NewsBulletinsIn(NewsBulletinsBase):
    pass
class NewsBulletinsOut(NewsBulletinsBase):
    articleID: int

class NewsKeywordsBase(BaseModel):
    keyword: Optional[str] = None
    numSearch: Optional[int] = None
class NewsKeywordsIn(NewsKeywordsBase):
    pass
class NewsKeywordsOut(NewsKeywordsBase):
    keyword: int

class OrderdetailsBase(BaseModel):
    orderID: Optional[int] = None
    productID: Optional[int] = None
    productNumber: Optional[str] = None
    productName: Optional[str] = None
    prodVarID: Optional[int] = None
    activityID: Optional[int] = None
    activityName: Optional[str] = None
    tournID: Optional[int] = None
    tournName: Optional[str] = None
    participantID: Optional[int] = None
    feedbackID: Optional[int] = None
    feedbackName: Optional[str] = None
    senderID: Optional[int] = None
    spec: Optional[str] = None
    textspec: Optional[str] = None
    quantity: Optional[int] = None
    unitprice: Optional[int] = None
    taxPros: Optional[int] = None
    subtotal: Optional[int] = None
    memberRecID: Optional[int] = None
class OrderdetailsIn(OrderdetailsBase):
    pass
class OrderdetailsOut(OrderdetailsBase):
    orderID: int

class OrdersBase(BaseModel):
    orderID: Optional[int] = None
    orderNum: Optional[str] = None
    paymentRef: Optional[str] = None
    payType: Optional[str] = None
    payMethod: Optional[str] = None
    maskedPan: Optional[str] = None
    cartID: Optional[str] = None
    customerID: Optional[int] = None
    custFname: Optional[str] = None
    custSname: Optional[str] = None
    custCompany: Optional[str] = None
    custAddress: Optional[str] = None
    custPostcode: Optional[str] = None
    custTown: Optional[str] = None
    custEmail: Optional[str] = None
    custPhone: Optional[str] = None
    custComments: Optional[str] = None
    shippingMethod: Optional[str] = None
    shippingPrice: Optional[int] = None
    admFee: Optional[int] = None
    admFeeDescription: Optional[str] = None
    boolCancelled: Optional[int] = None
    orderKey: Optional[str] = None
    confirmKey: Optional[str] = None
    dateCreated: Optional[int] = None
    boolCustConfirmed: Optional[int] = None
    dateCustConfirmed: Optional[int] = None
    boolShipped: Optional[int] = None
    dateShipped: Optional[int] = None
    boolClosed: Optional[int] = None
    dateClosed: Optional[int] = None
    closed_by: Optional[str] = None
    cancelled_by: Optional[str] = None
    sysComments: Optional[str] = None
    amountCharged: Optional[int] = None
    amountReserved: Optional[int] = None
    trigger_Webhook: Optional[int] = None
    reservedAmount: Optional[int] = None
    chargedAmount: Optional[int] = None
    chargeID: Optional[str] = None
    chargeDate: Optional[int] = None
    boolPaymentConfirmed: Optional[int] = None
    datePaymentConfirmed: Optional[int] = None
    boolEmailReceipt: Optional[int] = None
    payAccount: Optional[int] = None
    payLocal: Optional[int] = None
    boolRefunded: Optional[int] = None
    refundRef: Optional[str] = None
    refundAmount: Optional[int] = None
    refundDate: Optional[int] = None
class OrdersIn(OrdersBase):
    pass
class OrdersOut(OrdersBase):
    orderID: int

class PagesBase(BaseModel):
    pageID: Optional[int] = None
    parentID: Optional[int] = None
    depID: Optional[int] = None
    menuID: Optional[int] = None
    boolArchive: Optional[int] = None
    pluginID: Optional[int] = None
    plugin_ref: Optional[str] = None
    functionID: Optional[int] = None
    functionRef: Optional[str] = None
    fRefAlias: Optional[str] = None
    boolStart: Optional[int] = None
    boolShow: Optional[int] = None
    boolShowinmega: Optional[int] = None
    boolPrivacy: Optional[int] = None
    sortnum: Optional[int] = None
    template: Optional[int] = None
    templateID: Optional[int] = None
    boolImgZoom: Optional[int] = None
    boolDirectLink: Optional[int] = None
    directLink: Optional[str] = None
    boolExtLink: Optional[int] = None
    validfrom: Optional[int] = None
    validto: Optional[int] = None
    pagename: Optional[str] = None
    pagedescription: Optional[str] = None
    indexImageID: Optional[int] = None
    indexImage: Optional[str] = None
    indexImagePath: Optional[str] = None
    indeximg_descr: Optional[str] = None
    templateImageID: Optional[int] = None
    templateImage: Optional[str] = None
    templimg_descr: Optional[str] = None
    urlTitle: Optional[str] = None
    pageheading: Optional[str] = None
    pagecontent: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    date_modified: Optional[int] = None
    modified_by: Optional[str] = None
    videoUrl: Optional[str] = None
    teaser: Optional[str] = None
    boolInfoscreen: Optional[int] = None
    boolArchived: Optional[int] = None
    template_bgcolor: Optional[str] = None
    pageurlname: Optional[str] = None
    headerImage: Optional[str] = None
class PagesIn(PagesBase):
    pass
class PagesOut(PagesBase):
    pageID: int

class PagesMenusBase(BaseModel):
    menuID: Optional[int] = None
    depID: Optional[int] = None
    boolShow: Optional[int] = None
    menuheading: Optional[str] = None
    sortnum: Optional[int] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class PagesMenusIn(PagesMenusBase):
    pass
class PagesMenusOut(PagesMenusBase):
    menuID: int

class PagesPluginsBase(BaseModel):
    pageID: Optional[int] = None
    articleID: Optional[int] = None
    pluginID: Optional[int] = None
    pluginRef: Optional[int] = None
class PagesPluginsIn(PagesPluginsBase):
    pass
class PagesPluginsOut(PagesPluginsBase):
    pageID: int

class PaymentBase(BaseModel):
    orgnummer: Optional[str] = None
    boolOrdertoEmail: Optional[int] = None
    emailOrders: Optional[str] = None
    boolDibs: Optional[int] = None
    DibsMerchantID: Optional[str] = None
    Dibs_description: Optional[str] = None
    feeDibs: Optional[int] = None
    Dibs_test: Optional[int] = None
    boolKlarna_invoice: Optional[int] = None
    boolKlarna_account: Optional[int] = None
    KlarnaMerchantID: Optional[str] = None
    KlarnaSecret: Optional[str] = None
    feeKlarna_invoice: Optional[int] = None
    Klarna_inv_description: Optional[str] = None
    feeKlarna_account: Optional[int] = None
    Klarna_acc_description: Optional[str] = None
    boolLocalhandling: Optional[int] = None
    feeLocalhandling: Optional[int] = None
    Local_description: Optional[str] = None
    terms: Optional[str] = None
class PaymentIn(PaymentBase):
    pass
class PaymentOut(PaymentBase):
    orgnummer: int

class PhotoalbumBase(BaseModel):
    categoryID: Optional[int] = None
    depID: Optional[int] = None
    boolShow: Optional[int] = None
    albumname: Optional[str] = None
    urlAlias: Optional[str] = None
    sortnum: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class PhotoalbumIn(PhotoalbumBase):
    pass
class PhotoalbumOut(PhotoalbumBase):
    categoryID: int

class PhotoalbumImagesBase(BaseModel):
    imageID: Optional[int] = None
    categoryID: Optional[int] = None
    boolShow: Optional[int] = None
    imagefile: Optional[str] = None
    imgWidth: Optional[str] = None
    imgHeight: Optional[str] = None
    imgDescription: Optional[str] = None
    sortnum: Optional[str] = None
class PhotoalbumImagesIn(PhotoalbumImagesBase):
    pass
class PhotoalbumImagesOut(PhotoalbumImagesBase):
    imageID: int

class PluginsBase(BaseModel):
    pluginID: Optional[int] = None
    pluginPagefile: Optional[str] = None
    pluginFunction: Optional[str] = None
    pluginName: Optional[str] = None
    pluginMain: Optional[str] = None
    areaID: Optional[int] = None
    categoryID: Optional[int] = None
    sortnum: Optional[int] = None
    superv: Optional[int] = None
class PluginsIn(PluginsBase):
    pass
class PluginsOut(PluginsBase):
    pluginID: int

class PluginsCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    pluginCat: Optional[str] = None
class PluginsCategoriesIn(PluginsCategoriesBase):
    pass
class PluginsCategoriesOut(PluginsCategoriesBase):
    categoryID: int

class ProfilesBase(BaseModel):
    profileID: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    imageID: Optional[int] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    descr: Optional[str] = None
    myFacebook: Optional[str] = None
    myInsta: Optional[str] = None
    myScangolf: Optional[str] = None
    myLinkedin: Optional[str] = None
    myTwitter: Optional[str] = None
    myYoutube: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class ProfilesIn(ProfilesBase):
    pass
class ProfilesOut(ProfilesBase):
    profileID: int

class SetupBasicBase(BaseModel):
    clubname: Optional[str] = None
    address: Optional[str] = None
    postcode: Optional[str] = None
    city: Optional[str] = None
    orgnr: Optional[str] = None
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    urlContact: Optional[str] = None
    defibrillator: Optional[int] = None
    memberSignupTo: Optional[str] = None
    memberSignupTo_cc: Optional[str] = None
    memberTerms: Optional[str] = None
    memberOnlinePay: Optional[int] = None
    course_condition: Optional[str] = None
    ccond_url: Optional[str] = None
    ccond_image: Optional[str] = None
    ccond_validfrom: Optional[int] = None
    ccond_validto: Optional[int] = None
    blogDescr: Optional[str] = None
    blogNumInWidget: Optional[int] = None
    extraMailMsg: Optional[str] = None
    memberSelPayPeriode: Optional[int] = None
    geoHeight: Optional[str] = None
    ccon_selreport: Optional[str] = None
    ccon_rssurl: Optional[str] = None
class SetupBasicIn(SetupBasicBase):
    pass
class SetupBasicOut(SetupBasicBase):
    clubname: int

class SetupBasicReceiversBase(BaseModel):
    recID: Optional[int] = None
    receiver: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    sortnum: Optional[int] = None
    mainContact: Optional[int] = None
class SetupBasicReceiversIn(SetupBasicReceiversBase):
    pass
class SetupBasicReceiversOut(SetupBasicReceiversBase):
    recID: int

class SetupLanguageBase(BaseModel):
    langCode: Optional[str] = None
    language: Optional[str] = None
    localurl: Optional[str] = None
class SetupLanguageIn(SetupLanguageBase):
    pass
class SetupLanguageOut(SetupLanguageBase):
    langCode: int

class SetupPaymentBase(BaseModel):
    email_orders: Optional[str] = None
    email_orders_cc: Optional[str] = None
    boolLocal: Optional[int] = None
    localDescr: Optional[str] = None
    local_fee: Optional[int] = None
    boolNets: Optional[int] = None
    Nets_testmodus: Optional[int] = None
    Nets_merchantID: Optional[str] = None
    Nets_secretkey_live: Optional[str] = None
    Nets_checkoutkey_live: Optional[str] = None
    Nets_secretkey_test: Optional[str] = None
    Nets_checkoutkey_test: Optional[str] = None
    terms: Optional[str] = None
    boolCharge: Optional[int] = None
    accID: Optional[int] = None
    accountName: Optional[str] = None
    companyAdr: Optional[str] = None
    pcode: Optional[str] = None
    city: Optional[str] = None
    orgnr: Optional[str] = None
    boolOrder_byemail: Optional[int] = None
class SetupPaymentIn(SetupPaymentBase):
    pass
class SetupPaymentOut(SetupPaymentBase):
    email_orders: int

class SetupSiteBase(BaseModel):
    amtNewsMainFront: Optional[int] = None
    amtNewsDepFront: Optional[int] = None
    amtNewsPri: Optional[int] = None
    newsPriBig: Optional[int] = None
    siteDescription: Optional[str] = None
    fb_Url: Optional[str] = None
    fb_AppId: Optional[str] = None
    fb_AdminID: Optional[str] = None
    fb_AppSecret: Optional[str] = None
    fb_pixelID: Optional[str] = None
    google_Verification: Optional[str] = None
    google_AnalyticsID: Optional[str] = None
    google_API_KEY: Optional[str] = None
    insta_Url: Optional[str] = None
    twitter_Url: Optional[str] = None
    youtube_Url: Optional[str] = None
    snapchat_Url: Optional[str] = None
    topLanguage: Optional[int] = None
    topSearch: Optional[int] = None
    topUser: Optional[int] = None
    topSocial: Optional[int] = None
    topWeather: Optional[int] = None
    weather_url: Optional[str] = None
    spotify_Url: Optional[str] = None
    google_Tagmanager: Optional[str] = None
    title_front: Optional[str] = None
    yr_url: Optional[str] = None
    googleMapCode: Optional[str] = None
    longitude: Optional[str] = None
    latitude: Optional[str] = None
    geoHeight: Optional[str] = None
    yr_widgetBG: Optional[str] = None
    hioOnlyYear: Optional[int] = None
    linkedIn_Url: Optional[str] = None
    newsTemplate: Optional[int] = None
    useInfoscreen: Optional[int] = None
    fb_PageID: Optional[str] = None
    useCSbooking: Optional[int] = None
class SetupSiteIn(SetupSiteBase):
    pass
class SetupSiteOut(SetupSiteBase):
    amtNewsMainFront: int

class ShopCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    category: Optional[str] = None
    boolShow: Optional[int] = None
    urlAlias: Optional[str] = None
    sortnum: Optional[int] = None
class ShopCategoriesIn(ShopCategoriesBase):
    pass
class ShopCategoriesOut(ShopCategoriesBase):
    categoryID: int

class ShopProductsBase(BaseModel):
    productID: Optional[int] = None
    parentID: Optional[int] = None
    boolExpired: Optional[int] = None
    boolShow: Optional[int] = None
    boolForSale: Optional[int] = None
    boolVariants: Optional[int] = None
    boolTextvariant: Optional[int] = None
    boolLimitOne: Optional[int] = None
    boolShipping: Optional[int] = None
    custSpecText: Optional[str] = None
    sortnum: Optional[str] = None
    pricePrefix: Optional[str] = None
    priceOffset: Optional[int] = None
    textvarlabel: Optional[str] = None
    boolTextvarRequired: Optional[int] = None
    productName: Optional[str] = None
    variant: Optional[str] = None
    urlAlias: Optional[str] = None
    taxCode: Optional[int] = None
    price: Optional[int] = None
    price_std: Optional[int] = None
    boolPrice_camp: Optional[int] = None
    price_camp: Optional[int] = None
    campFromdate: Optional[int] = None
    campTodate: Optional[int] = None
    stock: Optional[str] = None
    shortdescr: Optional[str] = None
    description: Optional[str] = None
    datereg: Optional[int] = None
    creator: Optional[str] = None
    categoryID: Optional[int] = None
    boolLocalSaleOnly: Optional[int] = None
class ShopProductsIn(ShopProductsBase):
    pass
class ShopProductsOut(ShopProductsBase):
    productID: int

class ShopProductsImagesBase(BaseModel):
    imageID: Optional[int] = None
    productID: Optional[int] = None
    imagefile: Optional[str] = None
    sortnum: Optional[int] = None
    imgDescription: Optional[str] = None
class ShopProductsImagesIn(ShopProductsImagesBase):
    pass
class ShopProductsImagesOut(ShopProductsImagesBase):
    imageID: int

class ShopProductvargroupBase(BaseModel):
    productID: Optional[int] = None
    vargroupID: Optional[int] = None
class ShopProductvargroupIn(ShopProductvargroupBase):
    pass
class ShopProductvargroupOut(ShopProductvargroupBase):
    productID: int

class ShopSetupBase(BaseModel):
    boolCategories: Optional[int] = None
    payment_Nets: Optional[int] = None
    payment_Local: Optional[int] = None
    payment_Local_Descr: Optional[str] = None
    mailMessage: Optional[str] = None
class ShopSetupIn(ShopSetupBase):
    pass
class ShopSetupOut(ShopSetupBase):
    boolCategories: int

class ShopShippingsBase(BaseModel):
    shippingID: Optional[int] = None
    boolShow: Optional[int] = None
    shippingMethod: Optional[str] = None
    price: Optional[int] = None
    sortnum: Optional[int] = None
class ShopShippingsIn(ShopShippingsBase):
    pass
class ShopShippingsOut(ShopShippingsBase):
    shippingID: int

class ShopVargroupsBase(BaseModel):
    varGroupID: Optional[int] = None
    groupname: Optional[str] = None
class ShopVargroupsIn(ShopVargroupsBase):
    pass
class ShopVargroupsOut(ShopVargroupsBase):
    varGroupID: int

class SimTournamentScoreBase(BaseModel):
    scoreID: Optional[int] = None
    tournID: Optional[int] = None
    playerID: Optional[int] = None
    hcp: Optional[int] = None
    netto: Optional[int] = None
    brutto: Optional[int] = None
class SimTournamentScoreIn(SimTournamentScoreBase):
    pass
class SimTournamentScoreOut(SimTournamentScoreBase):
    scoreID: int

class SimTournamentSignupsBase(BaseModel):
    signupID: Optional[int] = None
    playerID: Optional[int] = None
    tournID: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    onWaitlist: Optional[int] = None
class SimTournamentSignupsIn(SimTournamentSignupsBase):
    pass
class SimTournamentSignupsOut(SimTournamentSignupsBase):
    signupID: int

class SimTournamentsBase(BaseModel):
    tournID: Optional[int] = None
    tourID: Optional[int] = None
    boolShow: Optional[int] = None
    tournname: Optional[str] = None
    urlTitle: Optional[str] = None
    tourndate: Optional[int] = None
    time_from: Optional[str] = None
    coursename: Optional[str] = None
    maxParticipants: Optional[str] = None
    partReserved: Optional[str] = None
    tournDescription: Optional[str] = None
    boolWaitlist: Optional[int] = None
    signup_from: Optional[int] = None
    signup_to: Optional[int] = None
    boolTeeTimePubl: Optional[int] = None
    boolResPubl: Optional[int] = None
class SimTournamentsIn(SimTournamentsBase):
    pass
class SimTournamentsOut(SimTournamentsBase):
    tournID: int

class SimTourplayersBase(BaseModel):
    playerID: Optional[int] = None
    tourID: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    hcp: Optional[int] = None
class SimTourplayersIn(SimTourplayersBase):
    pass
class SimTourplayersOut(SimTourplayersBase):
    playerID: int

class SimToursBase(BaseModel):
    tourID: Optional[int] = None
    depID: Optional[int] = None
    tourname: Optional[str] = None
    urlTitle: Optional[str] = None
    boolShow: Optional[int] = None
    sortnum: Optional[int] = None
class SimToursIn(SimToursBase):
    pass
class SimToursOut(SimToursBase):
    tourID: int

class SiteusersPwdtempBase(BaseModel):
    username: Optional[str] = None
    useremail: Optional[str] = None
    pwdkey: Optional[str] = None
    date_valid: Optional[int] = None
class SiteusersPwdtempIn(SiteusersPwdtempBase):
    pass
class SiteusersPwdtempOut(SiteusersPwdtempBase):
    username: int

class SiteusersSubscrBase(BaseModel):
    userID: Optional[int] = None
    depID: Optional[int] = None
class SiteusersSubscrIn(SiteusersSubscrBase):
    pass
class SiteusersSubscrOut(SiteusersSubscrBase):
    userID: int

class SponsorsBase(BaseModel):
    sponsorID: Optional[int] = None
    boolShow: Optional[int] = None
    sponsor: Optional[str] = None
    logofile: Optional[str] = None
    url: Optional[str] = None
    sortnum: Optional[int] = None
    sponsorDescr: Optional[str] = None
    categoryID: Optional[int] = None
class SponsorsIn(SponsorsBase):
    pass
class SponsorsOut(SponsorsBase):
    sponsorID: int

class SponsorsCategoriesBase(BaseModel):
    categoryID: Optional[int] = None
    category: Optional[str] = None
    sortnum: Optional[int] = None
    boolPri: Optional[int] = None
    sizecat: Optional[int] = None
class SponsorsCategoriesIn(SponsorsCategoriesBase):
    pass
class SponsorsCategoriesOut(SponsorsCategoriesBase):
    categoryID: int

class StatusCourseclubBase(BaseModel):
    boolCourse9: Optional[int] = None
    txtCourse9: Optional[str] = None
    boolSimCenter: Optional[int] = None
    txtSimCenter: Optional[str] = None
    boolRange: Optional[int] = None
    txtRange: Optional[str] = None
    boolPracticeOut: Optional[int] = None
    txtPracticeOut: Optional[str] = None
    boolPracticeIn: Optional[int] = None
    txtPracticeIn: Optional[str] = None
    boolPracticeGreen: Optional[int] = None
    txtPracticeGreen: Optional[str] = None
    selGreenQ: Optional[str] = None
    txtGreenQ: Optional[str] = None
    boolBallplacing: Optional[int] = None
    txtBallplacing: Optional[str] = None
    boolLessons: Optional[int] = None
    txtLessons: Optional[str] = None
    boolCafe: Optional[int] = None
    txtCafe: Optional[str] = None
    boolShop: Optional[int] = None
    txtShop: Optional[str] = None
    boolKiosk: Optional[int] = None
    txtKiosk: Optional[str] = None
    boolOffice: Optional[int] = None
    txtOffice: Optional[str] = None
class StatusCourseclubIn(StatusCourseclubBase):
    pass
class StatusCourseclubOut(StatusCourseclubBase):
    boolCourse9: int

class StatusInfoBase(BaseModel):
    statusID: Optional[int] = None
    statusLabel: Optional[str] = None
    boolOpen: Optional[int] = None
    statusText: Optional[str] = None
    sortnum: Optional[int] = None
class StatusInfoIn(StatusInfoBase):
    pass
class StatusInfoOut(StatusInfoBase):
    statusID: int

class TaxcodesBase(BaseModel):
    taxCode: Optional[int] = None
    taxPros: Optional[int] = None
class TaxcodesIn(TaxcodesBase):
    pass
class TaxcodesOut(TaxcodesBase):
    taxCode: int

class TemplateContentBase(BaseModel):
    templateID: Optional[int] = None
    template: Optional[str] = None
    col_left: Optional[str] = None
    col_right: Optional[str] = None
class TemplateContentIn(TemplateContentBase):
    pass
class TemplateContentOut(TemplateContentBase):
    templateID: int

class TourPlayersBase(BaseModel):
    recID: Optional[int] = None
    tourID: Optional[int] = None
    tournID: Optional[int] = None
    playerID: Optional[int] = None
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    hcp: Optional[int] = None
class TourPlayersIn(TourPlayersBase):
    pass
class TourPlayersOut(TourPlayersBase):
    recID: int

class TourScoresBase(BaseModel):
    scoreID: Optional[int] = None
    tourID: Optional[int] = None
    tournID: Optional[int] = None
    playerID: Optional[int] = None
    par: Optional[int] = None
    hcp: Optional[int] = None
    brutto: Optional[int] = None
    netto: Optional[int] = None
    points: Optional[int] = None
class TourScoresIn(TourScoresBase):
    pass
class TourScoresOut(TourScoresBase):
    scoreID: int

class TournamentsBase(BaseModel):
    tournID: Optional[int] = None
    listID: Optional[int] = None
    tourID: Optional[int] = None
    boolShow: Optional[int] = None
    tournName: Optional[str] = None
    tournAlias: Optional[str] = None
    location: Optional[str] = None
    tournDescription: Optional[str] = None
    date_start: Optional[int] = None
    time_from: Optional[str] = None
    time_to: Optional[str] = None
    boolGolfboxSignup: Optional[int] = None
    gbTournID: Optional[int] = None
    boolOnlineSignup: Optional[int] = None
    formID: Optional[int] = None
    boolOnlinePay: Optional[int] = None
    boolWaitlist: Optional[int] = None
    maxParticipants: Optional[str] = None
    partReserved: Optional[str] = None
    signup_from: Optional[int] = None
    signup_to: Optional[int] = None
    boolSuCouple: Optional[int] = None
    boolSuTeetime: Optional[int] = None
    boolSuHomeclub: Optional[int] = None
    boolSuPhone: Optional[int] = None
    boolSuBornyear: Optional[int] = None
    boolSignupToMail: Optional[int] = None
    signupMailTo: Optional[str] = None
    date_created: Optional[int] = None
    boolTeeTimePubl: Optional[int] = None
    teeTimeLink: Optional[str] = None
    boolTeeTimeLinkExt: Optional[int] = None
    boolResPubl: Optional[int] = None
    resLink: Optional[str] = None
    boolResLinkExt: Optional[int] = None
    refnr: Optional[str] = None
    created_by: Optional[str] = None
    boolExternal: Optional[int] = None
    priceGroupID: Optional[int] = None
    boolSuHcp: Optional[int] = None
    boolSuMembernum: Optional[int] = None
    boolShowSignups: Optional[int] = None
class TournamentsIn(TournamentsBase):
    pass
class TournamentsOut(TournamentsBase):
    tournID: int

class TournamentsListBase(BaseModel):
    listID: Optional[int] = None
    depID: Optional[int] = None
    sortnum: Optional[int] = None
    tourID: Optional[int] = None
    listname: Optional[str] = None
    urlTitle: Optional[str] = None
    listDescription: Optional[str] = None
    listYear: Optional[str] = None
    gb_customerid: Optional[str] = None
    boolGbList: Optional[int] = None
    gbListUrl: Optional[str] = None
    boolShow: Optional[int] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
    listFilter: Optional[str] = None
    gbListID: Optional[str] = None
class TournamentsListIn(TournamentsListBase):
    pass
class TournamentsListOut(TournamentsListBase):
    listID: int

class TournamentsParticipantsBase(BaseModel):
    participantID: Optional[int] = None
    tournID: Optional[int] = None
    boolSuConfirmed: Optional[int] = None
    orderID: Optional[int] = None
    price: Optional[int] = None
    memberID: Optional[str] = None
    hcp: Optional[str] = None
    fname: Optional[str] = None
    sname: Optional[str] = None
    email: Optional[str] = None
    bornYear: Optional[str] = None
    telephone: Optional[str] = None
    homeClub: Optional[str] = None
    memberID_mark: Optional[str] = None
    fname_mark: Optional[str] = None
    sname_mark: Optional[str] = None
    bornYear_mark: Optional[str] = None
    hcp_mark: Optional[str] = None
    homeClub_mark: Optional[str] = None
    suTeeTime: Optional[str] = None
    comments: Optional[str] = None
    suVerified: Optional[int] = None
    onWaitlist: Optional[int] = None
    refnr: Optional[str] = None
    date_signup: Optional[int] = None
class TournamentsParticipantsIn(TournamentsParticipantsBase):
    pass
class TournamentsParticipantsOut(TournamentsParticipantsBase):
    participantID: int

class TournamentsResultsBase(BaseModel):
    tournID: Optional[int] = None
    boolHtml: Optional[int] = None
    result: Optional[str] = None
    created_by: Optional[str] = None
class TournamentsResultsIn(TournamentsResultsBase):
    pass
class TournamentsResultsOut(TournamentsResultsBase):
    tournID: int

class TournamentsScoreBase(BaseModel):
    scoreID: Optional[int] = None
    tournID: Optional[int] = None
    playerID: Optional[int] = None
    hcp: Optional[int] = None
    netto: Optional[int] = None
    brutto: Optional[int] = None
class TournamentsScoreIn(TournamentsScoreBase):
    pass
class TournamentsScoreOut(TournamentsScoreBase):
    scoreID: int

class TournamentsStartlistsBase(BaseModel):
    tournID: Optional[int] = None
    boolHtml: Optional[int] = None
    startlist: Optional[str] = None
    created_by: Optional[str] = None
class TournamentsStartlistsIn(TournamentsStartlistsBase):
    pass
class TournamentsStartlistsOut(TournamentsStartlistsBase):
    tournID: int

class WidgetsBase(BaseModel):
    widgetID: Optional[int] = None
    depID: Optional[int] = None
    widgetWidth: Optional[str] = None
    widgetName: Optional[str] = None
    widgetType: Optional[int] = None
    widgetFunction: Optional[str] = None
    widgetHeading: Optional[str] = None
    widgetContent: Optional[str] = None
    comments: Optional[str] = None
    date_created: Optional[int] = None
    created_by: Optional[str] = None
class WidgetsIn(WidgetsBase):
    pass
class WidgetsOut(WidgetsBase):
    widgetID: int

class WidgetsPlacedBase(BaseModel):
    widgetID: Optional[int] = None
    widgetType: Optional[int] = None
    depID: Optional[int] = None
    area: Optional[str] = None
    sortnum: Optional[int] = None
class WidgetsPlacedIn(WidgetsPlacedBase):
    pass
class WidgetsPlacedOut(WidgetsPlacedBase):
    widgetID: int

# -- AUTO GENERATED SCHEMAS END

#— (paste any other stub‐schemas from stubs.txt here) —
>>>>>>> 913c8f343c976e70c42f5237bb48b73aefda84fd
