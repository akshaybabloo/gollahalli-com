import datetime
import unittest.mock as mock
from io import BytesIO

import pytz
from PIL import Image
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase

from editor.models import ContentModel, EducationModel, ProjectsModel, TutorialsModel, ExperienceModel, SkillsModel, \
    SkillsContentModel, PublicationsModel, PublicationsContentModel, MetaContentModel


def mock_datetime_now():
    """
    Date and time with timezone.

    Returns
    -------
    datetime: datetime
        Datetime object.
    """
    return datetime.datetime(2013, 11, 20, 20, 8, 7, 127325, tzinfo=pytz.UTC)


def mock_date():
    """
    Mocks date.
    
    Returns
    -------
    datetime: datetime
        Datetime object.
    """
    return datetime.date(2013, 11, 20)


class ContentModelTest(TestCase):
    """
    Test case for `ContentModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `ContentModel` and mocks django `timezone`
        
        """
        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        ContentModel.objects.create(ref_id=1,
                                    website_name="Akshay Raj Gollahalli",
                                    cv=SimpleUploadedFile('best_file_eva.txt',
                                                          'these are the file contents!'.encode('utf-8')),
                                    bio="bio",
                                    url="https://www.example.com",
                                    first_name="Some name",
                                    last_name="last name",
                                    email_id="name@example.com",
                                    github="https://www.github.com",
                                    twitter="https://www.twitter.com",
                                    linkedin="https://www.linkedin.com",
                                    file=SimpleUploadedFile('content_model.txt',
                                                            'these are the file contents!'.encode('utf-8')),
                                    image=InMemoryUploadedFile(im_io, None, 'content_model.jpg', 'image/jpeg', im_io,
                                                               None))

    def test_model(self):
        """
        Tests `ref_id`, `website_name`, `bio`, `url`, `first_name`, `last_name`, `email_id`, `github`, `twitter` and 
        `linkedin`.

        """
        content = ContentModel.objects.get(ref_id=1)

        self.assertEqual(content.ref_id, 1)
        self.assertEqual(content.website_name, "Akshay Raj Gollahalli")
        self.assertEqual(content.bio, "bio")
        self.assertEqual(content.url, "https://www.example.com")
        self.assertEqual(content.first_name, "Some name")
        self.assertEqual(content.last_name, "last name")
        self.assertEqual(content.email_id, "name@example.com")
        self.assertEqual(content.github, "https://www.github.com")
        self.assertEqual(content.twitter, "https://www.twitter.com")
        self.assertEqual(content.linkedin, "https://www.linkedin.com")

    def test_timedate(self):
        """
        Tests `created` and `updated` date and time.
        """
        content = ContentModel.objects.get(ref_id=1)

        self.assertEqual(content.created, mock_datetime_now())
        self.assertEqual(content.updated, mock_datetime_now())

    def test_uploads(self):
        """
        Tests file uploads of `cv`, `file`, and `image`
        """
        content = ContentModel.objects.get(ref_id=1)

        self.assertEqual(content.cv, content.cv.name)
        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class EducationModelTest(TestCase):
    """
    Test case for `EducationModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `EducationModel` and mocks django `timezone`
        
        """

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        model = ContentModel.objects.create(ref_id=1)
        EducationModel.objects.create(id=1,
                                      ref_id=model,
                                      title="some title",
                                      from_date=mock_date(),
                                      to_date=mock_date(),
                                      where="somewhere",
                                      current=True,
                                      file=SimpleUploadedFile('education_model.txt',
                                                              'these are the file contents!'.encode('utf-8')),
                                      image=InMemoryUploadedFile(im_io, None, 'education_model.jpg', 'image/jpeg',
                                                                 im_io,
                                                                 None))

    def test_model(self):
        """
        Tests `id`, `title`, `from_date`, `to_date`, `where` and `current`.
        """
        content = EducationModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.title, "some title")
        self.assertEqual(content.from_date, mock_date())
        self.assertEqual(content.to_date, mock_date())
        self.assertEqual(content.where, "somewhere")
        self.assertEqual(content.current, True)

    def test_files(self):
        """
        Tests `file` and `image`.
        """
        content = EducationModel.objects.get(id=1)

        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class ProjectsModelTest(TestCase):
    """
    Test case for `ProjectsModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `ProjectsModel` and mocks django `timezone`

        """

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        model = ContentModel.objects.create(ref_id=1)
        ProjectsModel.objects.create(id=1,
                                     ref_id=model,
                                     link="https://www.example.com",
                                     title="some title",
                                     category="some category",
                                     long_description="very long description\n yes very long",
                                     short_description="short description",
                                     file=SimpleUploadedFile('project_model.txt',
                                                             'these are the file contents!'.encode('utf-8')),
                                     image=InMemoryUploadedFile(im_io, None, 'project_model.jpg', 'image/jpeg',
                                                                im_io,
                                                                None))

    def test_model(self):
        """
        Tests `id`, `link`, `title`, `category`, `long_description`, and `short_description`
        """

        content = ProjectsModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.link, "https://www.example.com")
        self.assertEqual(content.title, "some title")
        self.assertEqual(content.category, "some category")
        self.assertEqual(content.long_description, "very long description\n yes very long")
        self.assertEqual(content.short_description, "short description")

    def test_files(self):
        """
        Tests `file` and `image`.
        """

        content = ProjectsModel.objects.get(id=1)

        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class TutorialsModelTest(TestCase):
    """
    Test case for `TutorialsModel`
    """

    def setUp(self):
        """
        Sets up the `TutorialsModel` and mocks django `timezone`

        """

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        model = ContentModel.objects.create(ref_id=1)
        TutorialsModel.objects.create(id=1,
                                      ref_id=model,
                                      link="https://www.example.com",
                                      title="some title",
                                      long_description="very long description\n yes very long",
                                      file=SimpleUploadedFile('tutorials_model.txt',
                                                              'these are the file contents!'.encode('utf-8')),
                                      image=InMemoryUploadedFile(im_io, None, 'tutorials_model.jpg', 'image/jpeg',
                                                                 im_io,
                                                                 None))

    def test_model(self):
        """
        Tests `id`, `link`, `title` and `long_description`
        """

        content = TutorialsModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.link, "https://www.example.com")
        self.assertEqual(content.title, "some title")
        self.assertEqual(content.long_description, "very long description\n yes very long")

    def test_files(self):
        """
        Tests `file` and `image`.
        """

        content = TutorialsModel.objects.get(id=1)

        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class ExperienceModelTest(TestCase):
    """
    Test case for `ExperienceModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `ExperienceModel` and mocks django `timezone`

        """

        model = ContentModel.objects.create(ref_id=1)
        ExperienceModel.objects.create(id=1,
                                       ref_id=model,
                                       title="some title",
                                       from_date=mock_date(),
                                       to_date=mock_date(),
                                       where_city="some city",
                                       where_country="some country",
                                       current=True,
                                       company="some company")

    def test_model(self):
        """
        Tests `id`, `title`, `from_date`, `to_date`, `where_city`, `where_country`, `company` and `current`.
        """
        content = ExperienceModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.title, "some title")
        self.assertEqual(content.from_date, mock_date())
        self.assertEqual(content.to_date, mock_date())
        self.assertEqual(content.where_city, "some city")
        self.assertEqual(content.where_country, "some country")
        self.assertEqual(content.company, "some company")
        self.assertEqual(content.current, True)


class SkillsModelTest(TestCase):
    """
    Test case for `SkillsModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `SkillsModel` and mocks django `timezone`

        """

        model = ContentModel.objects.create(ref_id=1)
        SkillsModel.objects.create(ref_id=model, type_of_skill="some type")

    def test_model(self):
        """
        Tests `type_of_skill`
        """

        content = SkillsModel.objects.get(type_of_skill="some type")

        self.assertEqual(content.type_of_skill, "some type")


class SkillsContentModelTest(TestCase):
    """
    Test case for `SkillsContentModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `SkillsContentModel` and mocks django `timezone`

        """

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        model = ContentModel.objects.create(ref_id=1)
        skills_model = SkillsModel.objects.create(ref_id=model, type_of_skill="some type")
        SkillsContentModel.objects.create(id=1,
                                          type_of_skill=skills_model,
                                          content="some content",
                                          file=SimpleUploadedFile('skills_content_model.txt',
                                                                  'these are the file contents!'.encode('utf-8')),
                                          image=InMemoryUploadedFile(im_io, None, 'skills_content_model.jpg',
                                                                     'image/jpeg',
                                                                     im_io,
                                                                     None))

    def test_model(self):
        """
        Tests `id` and `content`
        """

        content = SkillsContentModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.content, "some content")

    def test_files(self):
        """
        Tests `file` and `image`.
        """
        content = SkillsContentModel.objects.get(id=1)

        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class PublicationsModelTest(TestCase):
    """
    Test case for `PublicationsModel`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `PublicationsModel` and mocks django `timezone`

        """

        model = ContentModel.objects.create(ref_id=1)
        PublicationsModel.objects.create(ref_id=model, type_of_publication="some publication")

    def test_model(self):
        """
        Tests `type_of_publication`
        """

        content = PublicationsModel.objects.get(type_of_publication="some publication")

        self.assertEqual(content.type_of_publication, "some publication")


class PublicationsContentModelTest(TestCase):
    """
    Test case for `PublicationsContentMode`
    """

    @mock.patch('django.utils.timezone.now', mock_datetime_now)
    def setUp(self):
        """
        Sets up the `PublicationsModel` and mocks django `timezone`

        """

        im = Image.new(mode='RGB', size=(200, 200))  # create a new image using PIL
        im_io = BytesIO()  # a BytesIO object for saving image
        im.save(im_io, 'JPEG')  # save the image to im_io
        im_io.seek(0)

        model = ContentModel.objects.create(ref_id=1)
        publication_model = PublicationsModel.objects.create(ref_id=model, type_of_publication="some publication")
        PublicationsContentModel.objects.create(id=1,
                                                type_of_publication=publication_model,
                                                content="some content",
                                                file=SimpleUploadedFile('publication_content_model.txt',
                                                                        'these are the file contents!'.encode('utf-8')),
                                                image=InMemoryUploadedFile(im_io, None, 'publication_content_model.jpg',
                                                                           'image/jpeg',
                                                                           im_io,
                                                                           None))

    def test_model(self):
        """
        Tests `id` and `content`
        """

        content = PublicationsContentModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.content, "some content")

    def test_files(self):
        """
        Tests `file` and `image`.
        """
        content = PublicationsContentModel.objects.get(id=1)

        self.assertEqual(content.file, content.file.name)
        self.assertEqual(content.image, content.image.name)


class MetaContentModelTest(TestCase):
    """
    Test case for `MetaContentModel`
    """

    def setUp(self):
        """
        Sets up `MetaContentModel`
        """
        MetaContentModel.objects.create(id=1,
                                        header="some header",
                                        footer="some footer",
                                        meta="some meta")

    def test_model(self):
        """
        Tests `id`, `header`, `footer` and `meta`
        """
        content = MetaContentModel.objects.get(id=1)

        self.assertEqual(content.id, 1)
        self.assertEqual(content.header, "some header")
        self.assertEqual(content.footer, "some footer")
        self.assertEqual(content.meta, "some meta")
