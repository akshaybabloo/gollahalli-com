"""
Serializes and makes a zip file to back up the data.
"""
from gollahalli_com.schema import query
import json

QUERY = '''
        {
          allContents {
            refId
            created
            updated
            websiteName
            cv
            bio
            url
            firstName
            lastName
            emailId
            github
            twitter
            linkedin
            file
            image
            education {
              id
              title
              fromDate
              toDate
              where
              current
              file
              image
            }
            projects {
              id
              link
              title
              category
              longDescription
              shortDescription
              file
              image
            }
            tutorials {
              id
              link
              title
              longDescription
              file
              image
            }
            experience {
              id
              fromDate
              toDate
              title
              whereCity
              whereCountry
              company
              current
            }
            skills {
              skillsContent {
                id
                typeOfSkill {
                  typeOfSkill
                }
                content
                file
                image
              }
            }
            publications {
              publicationsContent {
                id
                typeOfPublication {
                  typeOfPublication
                }
                content
                file
                image
              }
            }
          }
          allMetaContent {
            id
            header
            footer
            meta
          }
        }

        '''


class Serialize:
    def __init__(self):
        self.data = query.execute(QUERY)
        self.data = json.dumps(self.data.data)

    def dump(self, files=False, verbose=False):
        pass

    def __zip(self):
        pass

    def __get_files(self):
        pass

    def log(self):
        print(self.data)

    def loads(self, verbose=False):
        pass

    def __unzip(self):
        pass

    def __put_files(self):
        pass
