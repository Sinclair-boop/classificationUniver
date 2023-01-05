import graphene
from graphene_django import DjangoObjectType

from .models import UniversityModel


class UniversityType(DjangoObjectType):
    class Meta:
        model = UniversityModel


class Query(graphene.ObjectType):
    universities = graphene.List(UniversityType)

    def resolve_universities(self, info):
        return UniversityModel.objects.all()


# schema = graphene.Schema(query=Query)

# Using mutation
class CreateUniversity(graphene.Mutation):
    id = graphene.Int()
    university_name = graphene.String()
    university_link = graphene.String()

    class Arguments:
        university_name = graphene.String()
        university_link = graphene.String()

    def mutate(self, info, university_name, university_link):
        university = UniversityModel(university_name=university_name, university_link=university_link)
        university.save()

        return CreateUniversity(
            id=university.id,
            university_name=university.university_name,
            university_link=university.university_link,
        )


class Mutation(graphene.ObjectType):
    create_university = CreateUniversity.Field()


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)


schema = graphene.Schema(
    query=Query,
    mutation=Mutation
)


# mutation createUniversity($university_name: String, $university_link: String){
#   createUniversity(university_name: $university_name, University_link: $University_link) {
#     id
#     university_name
#     university_name
#   }
# }