from /Login/models import Userdetail

# test user details
u1d = Userdetail.objects.create(Fname='John',Lname='Doe',Techlevel='1',Year='1',Rating='1',
                                Bio='test is life',Instruments='Guitar',Genre='Rock'}
u2d = Userdetail.objects.create(Fname='Jane',Lname='Doe',Techlevel='2',Year='2',Rating='2',
                                Bio='life is a test',Instruments='Violin',Genre='Classical'}
u3d = Userdetail.objects.create(Fname='Chi',Lname='Shin',Techlevel='3',Year='3',Rating='3',
                                Bio='So many tests!',Instruments='Drums',Genre='Punk'}