from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User, UserManager
import datetime

# Create your models here.

#######################################   Catalogs  ################################################  
####################################################################################################
class Region(TimeStampedModel):
  """(Region description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  
  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Currency(TimeStampedModel):
  """(Currency description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  
  class Meta:
      verbose_name_plural = "Currencies"
  
  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Sector(TimeStampedModel):
  """(Sector description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Activity(TimeStampedModel):
  """(Activity description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
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
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  class Meta:
      verbose_name_plural = "Categories"

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class WorkItem(TimeStampedModel):
  """(WorkItem description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  is_delib    = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class ProjectType(TimeStampedModel):
  """ProjectType """
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class ProjectStatus(TimeStampedModel):
  """(ProjectStatus description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  customer    = models.ForeignKey('Company')
#  next_statues

  class Meta:
      verbose_name_plural = "Project Statuses"

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)





#######################################   Domain  ##################################################  
####################################################################################################
class Employee(User):
  """(Employee description)"""
  MARITAL_STATUS = (
      (u'M', u'Married'),
      (u'S', u'Single'),
  )
  salary         = models.DecimalField(max_digits=15, decimal_places=4)
  is_Manager     = models.BooleanField(default=True)
  telephone      = models.CharField(blank=True, max_length=15)
  birth_date     = models.DateField(default=datetime.datetime.today)
  contract_date  = models.DateField(default=datetime.datetime.today)
  comments       = models.TextField(blank=True)
  has_passport   = models.BooleanField(default=True)      
  is_technical   = models.BooleanField(default=True)   
  can_travel     = models.BooleanField(default=True)
  english_level  = models.CharField(blank=True, max_length=30)
  marital_status = models.CharField(max_length=15, choices=MARITAL_STATUS) 
  # Relationships
  region         = models.ForeignKey(Region)

  def __unicode__(self):
    return u"%s, %s" % (self.first_name , self.last_name)


####################################################################################################
class WorkSession(TimeStampedModel):
  """This class represent a chunk of working time associated to some activity.
     We get more flexibility and by the way is easier to register.
  """
  work_date   = models.DateField(default=datetime.datetime.today)
  time        = models.PositiveIntegerField(blank=True, null=False)
  description = models.CharField(blank=True, max_length=100)
  comments    = models.TextField(blank=True) 
  billable    = models.BooleanField(default=True)
  # Relationships
  activity    = models.ForeignKey(Activity, blank=True, null=True) 
  category    = models.ForeignKey(Category)
  project     = models.ForeignKey('Project')
  employee    = models.ForeignKey(Employee) 
  #work_item   = models.ForeignKey(WorkItem) #TODO: We need to validate this

  def __unicode__(self):
    return u"%s" % (self.description)


####################################################################################################
class Company(TimeStampedModel):
  """(Company description)"""
  trade_name  = models.CharField(blank=True, max_length=80)
  legal_name  = models.CharField(blank=True, max_length=80)
  description = models.TextField(blank=True)
  rate        = models.DecimalField(max_digits=15, decimal_places=4)
  since       = models.DateField(default=datetime.datetime.today)
  address     = models.CharField(blank=True, max_length=100)
  is_customer = models.BooleanField(default=True)
  # Relationships
  sector      = models.ManyToManyField(Sector) 
  #contact     = models.ForeignKey(User) # Let us include it in another application (Contact manager?)
  admin_team  = models.ManyToManyField(Employee, related_name='company_admin_set') #TODO: Maybe let us create another application in order to assign managers (Staff manager?) 

  class Meta:
      verbose_name_plural = "Companies"

  def __unicode__(self):
    return u"%s" % (self.trade_name)


####################################################################################################
class BusinessUnit(TimeStampedModel):
  """(BusinessUnit description)"""
  name        = models.CharField(blank=True, max_length=80)
  description = models.CharField(blank=True, max_length=100)
  enabled     = models.BooleanField(default=True)
  # Relationships
  company     = models.ForeignKey(Company)
  parent      = models.ForeignKey('self', null=True, blank=True)
  customer_team = models.ManyToManyField(User)  #customer people in charge
  admin_team  = models.ManyToManyField(Employee, related_name='businessunit_admin_set' ) #TODO: Maybe let us create another application in order to assign managers (Staff manager?) 

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.description)


####################################################################################################
class Project(TimeStampedModel):
  """(Project description)"""
  name               = models.CharField(blank=True, max_length=80)
  alias              = models.CharField(blank=True, max_length=80) # name given by the client: folio, service order, execution request
  external_id        = models.CharField(blank=True, max_length=80) # identifier given by the client
  description        = models.CharField(blank=True, max_length=100)
  creation_date      = models.DateField(default=datetime.datetime.today) # when the project was internally approved by the client
  request_date       = models.DateField(default=datetime.datetime.today) # when we received the formal request by the client
  enabled            = models.BooleanField(default=True)
  planned_start_date = models.DateField(default=datetime.datetime.today)
  real_start_date    = models.DateField(default=datetime.datetime.today)
  planned_end_date   = models.DateField(default=datetime.datetime.today)
  real_end_date      = models.DateField(default=datetime.datetime.today)
  planned_effort     = models.PositiveIntegerField(blank=True, null=True)
  real_effort        = models.PositiveIntegerField(blank=True, null=True)
  budget             = models.DecimalField(max_digits=15, decimal_places=4) # costo
  references         = models.TextField(blank=True)  # links or other supplemental info 
  rate               = models.PositiveIntegerField(blank=True, null=True)
  exchange_rate      = models.PositiveIntegerField(blank=True, null=True)
  # Relationships
  currency           = models.ForeignKey(Currency)
  status             = models.ForeignKey(ProjectStatus) # canceled, active, suspended 
  customer           = models.ForeignKey(Company)
  region             = models.ForeignKey('Region') #Mexico, Monterrey, Guadalajara, EU
  team               = models.ManyToManyField(Employee, related_name='client_projects') # team assigned to the project
  admin_team         = models.ManyToManyField(Employee, related_name='project_admin_set' ) #TODO: Maybe let us create another application in order to assign managers (Staff manager?) 
  client_project_type= models.ForeignKey(ProjectType, related_name='projects')  # Clasificacion de nivel de requerimiento: N1, N2 N3, N4, N5
  internal_project_type= models.ForeignKey(ProjectType)  # Pruebas, Desarrollo, Analisis
  client_business_unit = models.ForeignKey(BusinessUnit, related_name='projects') # Dominio, etc.
  internal_business_unit = models.ForeignKey(BusinessUnit, related_name='internal_projects') # Testing, Development, etc.
  customer_contact     = models.ForeignKey(User, related_name='client_business_projects')

  #  milestones        #(Requerimiento funcional, entregable, fechas, etc.)
  #  work_items #(Applications, etc.)

  def __unicode__(self):
    return u"%s, %s" % (self.name , self.alias)

