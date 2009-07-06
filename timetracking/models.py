from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User, UserManager
import datetime

####################################################################################################
#######################################   Catalogs  ################################################  
####################################################################################################
class Region(TimeStampedModel):
  """Regions where we have operations"""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  
  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Currency(TimeStampedModel):
  """Currencies used in contracts"""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  
  class Meta:
      verbose_name_plural = "Currencies"
  
  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Sector(TimeStampedModel):
  """Business sectors"""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Activity(TimeStampedModel):
  """Activities that are predefined by the customer. As in Banorte."""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  billable    = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  class Meta:
      verbose_name_plural = "Activities"

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Category(TimeStampedModel):
  """(Category description)"""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  class Meta:
      verbose_name_plural = "Categories"

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class WorkItem(TimeStampedModel):
  """This could represent a project an artefact or whatever is produced as a result of a worksession"""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  is_deliverable = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class ProjectType(TimeStampedModel):
  """ProjectType """
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class ProjectStatus(TimeStampedModel):
  """The current project status. It doesn't have an historic record."""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  class Meta:
      verbose_name_plural = "Project Statuses"

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)

####################################################################################################
class Application(TimeStampedModel):
  """Customer's applications for a project."""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  class Meta:
      verbose_name_plural = "Applications"

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)



####################################################################################################
#######################################   Domain  ##################################################  
####################################################################################################
class Employee(User):
  """
  We use the django authorization model to represent our employess.
  We only define the extra fields required for our timetracking system.
  """
  MARITAL_STATUSES = (
      (u'M', u'Married'),
      (u'S', u'Single'),
  )
  ENGLISH_LEVELS = (
      (u'iBT TOEFL 107-120', u'iBT TOEFL 107-120'),
      (u'iBT TOEFL 90-106', u'iBT TOEFL 90-106'),
      (u'iBT TOEFL 61-89', u'iBT TOEFL 61-89'),
      (u'iBT TOEFL 57-60', u'iBT TOEFL 57-60'),
      (u'CPE', u'Cambridge-Certificate of Proficiency in English'),
      (u'CAE', u'Cambridge-Certificate in Advance English'),
      (u'FCE', u'Cambridge-First Certificate in English'),
      (u'PET', u'Cambridge-Preliminary English Test'),
      (u'KET', u'Cambridge-Key English Test'),
      (u'IELTS 7.5-9.0', u'International English Language Testing System 7.5-9.0'),
      (u'IELTS 6.5-7.0', u'International English Language Testing System 6.5-7.0'),
      (u'IELTS 5.0-6.0', u'International English Language Testing System 5.0-6.0'),
      (u'IELTS 3.5-4.5', u'International English Language Testing System 3.5-4.5'),
      (u'IELTS 3.0', u'International English Language Testing System 3.0'),
  )
  
  salary         = models.DecimalField(max_digits=15, decimal_places=4, help_text="Salary before taxes (Raw)")
  is_Manager     = models.BooleanField(default=False, help_text="Designates whether this user has a leadership or managerial rol")
  telephone      = models.CharField(blank=True, null=True, max_length=15)
  birth_date     = models.DateField(blank=True, null=True)
  contract_date  = models.DateField(default=datetime.datetime.now)
  comments       = models.TextField(blank=True, null=True)
  has_passport   = models.BooleanField(default=True)      
  is_technical   = models.BooleanField(default=False, help_text="Designates whether this user has a technical leadership rol")   
  can_travel     = models.BooleanField(default=False)
  english_level  = models.CharField(blank=True, null=True, max_length=50, choices=ENGLISH_LEVELS)
  marital_status = models.CharField(blank=True, null=True, max_length=15, choices=MARITAL_STATUSES) 
  # Relationships
  region         = models.ForeignKey(Region)

  def __unicode__(self):
    return u"%s, %s" % (self.first_name , self.last_name)


####################################################################################################
class WorkSession(TimeStampedModel):
  """
  This class represent a chunk of working time associated to one activity.
  We get more flexibility and by the way is easier to register than forcing to use the activity as the unit of work.
  In order to support diferent contexts the activity field is optional. In such case we will use the description field instead. 
  They are mutual exclusive (free or fixed style).
  """
  work_date   = models.DateField(default=datetime.datetime.today)
  time        = models.PositiveIntegerField(null=False)
  description = models.CharField(blank=True, default='', max_length=100)
  comments    = models.TextField(blank=True, default='') 
  billable    = models.BooleanField(default=True)
  # Relationships
  activity    = models.ForeignKey(Activity, blank=True, null=True) 
  work_item   = models.ForeignKey(WorkItem, blank=True, null=True, help_text="The time will be charged to this product.") 
  category    = models.ForeignKey(Category, blank=True, null=True, help_text="To which group we will charge this time.")
  project     = models.ForeignKey('Project')
  employee    = models.ForeignKey(Employee) 

  def __unicode__(self):
    return u"%s" % (self.description)


####################################################################################################
class Company(TimeStampedModel):
  """
  This class models any kind of company: Customer, Partners, Associates, including ourself.
  """
  RELATIONSHIP_TYPES = (
      (u'C', u'Customer'),
      (u'P', u'Partner'),
      (u'A', u'Associate'),
  )
  trade_name   = models.CharField(max_length=80, help_text="Common o comercial name. Used normally by marketing purposes")
  legal_name   = models.CharField(max_length=80, help_text="Name used for contracts") 
  description  = models.TextField(blank=True, null=True)
  service_rate = models.DecimalField(max_digits=15, decimal_places=4, help_text="General service rate. It is used as default when the project is created.")
  address      = models.CharField(blank=True, null=True, max_length=150)
  relationship_since = models.DateField(default=datetime.datetime.today, help_text="when the relationship began")
  relationship_type  = models.CharField(max_length=2, choices=RELATIONSHIP_TYPES)
  project_alias      = models.CharField(blank=True, null=True, max_length=80, help_text="Name of the project given by the client: folio, service order, execution request.")
  # Model Relationships
  sector       = models.ManyToManyField(Sector) 
  # contact     = models.ForeignKey(User) # Let us include it in another application (Contact manager?)
  # admin_team  = models.ManyToManyField(Employee, related_name='company_admin_set') #TODO: Maybe create another application in order to assign managers (Staff manager?) 

  class Meta:
      verbose_name_plural = "Companies"

  def __unicode__(self):
    return u"%s" % (self.trade_name)


####################################################################################################
class BusinessUnit(TimeStampedModel):
  """(BusinessUnit description)"""
  name        = models.CharField(max_length=80)
  description = models.CharField(max_length=100)
  enabled     = models.BooleanField(default=True)
  # Relationships
  company     = models.ForeignKey(Company, help_text="Company it belongs to")
  parent      = models.ForeignKey('self', null=True, blank=True, help_text="Another business unit it belongs to")
  customer_team = models.ManyToManyField(User, help_text="Customer's people in charge")
  #admin_team  = models.ManyToManyField(Employee, related_name='businessunit_admin_set' ) #TODO: Maybe let us create another application in order to assign managers (Staff manager?) 

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Project(TimeStampedModel):
  """(Project description)"""
  name               = models.CharField(max_length=80)
  external_id        = models.CharField(blank=True, null=True, max_length=80, help_text="Identifier given by the client") 
  description        = models.CharField(max_length=100)
  creation_date      = models.DateField(blank=True, null=True, default=datetime.datetime.today, help_text="When the project was internally approved by the client.") 
  request_date       = models.DateField(blank=True, null=True, default=datetime.datetime.today, help_text="When we received the formal request by the client.")
  enabled            = models.BooleanField(default=True)
  planned_start_date = models.DateField(blank=True, null=True, default=datetime.datetime.today)
  real_start_date    = models.DateField(blank=True, null=True, default=datetime.datetime.today)
  planned_end_date   = models.DateField(blank=True, null=True, default=datetime.datetime.today)
  real_end_date      = models.DateField(blank=True, null=True, default=datetime.datetime.today)
  planned_effort     = models.PositiveIntegerField(blank=True, null=True)
  real_effort        = models.PositiveIntegerField(blank=True, null=True)
  budget             = models.DecimalField(max_digits=15, decimal_places=4, help_text="Project cost")
  references         = models.TextField(blank=True, null=True, help_text="links or other supplemental info") 
  rate               = models.PositiveIntegerField(blank=True, null=True, help_text="Rate of the service. The default is given by the Customer.")
  exchange_rate      = models.PositiveIntegerField(blank=True, null=True, help_text="Exchange rate used to evaluate the cost of the project")
  # Relationships
  currency           = models.ForeignKey(Currency)
  status             = models.ForeignKey(ProjectStatus) # canceled, active, suspended 
  customer           = models.ForeignKey(Company)
  region             = models.ForeignKey(Region) #Mexico, Monterrey, Guadalajara, EU
  team               = models.ManyToManyField(Employee, related_name='client_projects') # team assigned to the project
  client_project_type   = models.ForeignKey(ProjectType, related_name='projects', help_text="Clasification given by the client: N1, N2 N3, N4, N5")
  internal_project_type = models.ForeignKey(ProjectType, help_text="Clasification given by us: Pruebas, Desarrollo, Analisis")
  client_business_unit  = models.ForeignKey(BusinessUnit, blank=True, null=True, related_name='projects') # Dominio, etc.
  internal_business_unit= models.ForeignKey(BusinessUnit, related_name='internal_projects', help_text="Testing, Development, etc.")
  customer_contact      = models.ForeignKey(User, related_name='client_business_projects')
  work_items            = models.ManyToManyField(WorkItem, blank=True, null=True, help_text="It could be applications, artefacts, etc.")
  #  admin_team         = models.ManyToManyField(Employee, related_name='project_admin_set' ) #TODO: Maybe let us create another application in order to assign managers (Staff manager?) 
  #  milestones        #(Requerimiento funcional, entregable, fechas, etc.)
  #  work_items #(Applications, etc.)

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.alias)

