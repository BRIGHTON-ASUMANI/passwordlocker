class User:

    #Class that generates new instances of users
    user_list = [] # Empty user list
    def __init__(self,first_name,last_name,email,username,password,confirmpassword):

      # docstring removed for simplicity

        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email
        self.password = password
        self.confirmpassword = confirmpassword

    def save_user(self):

        '''
        save_user method saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self)

    @classmethod
    def find_by_email(cls,email):
        '''
        Method that takes in an email and returns a user that matches that email.

        Args:
            number: email to search for
        Returns :
            User of person that matches the email.
        '''

        for user in cls.user_list:
            if user.email == email:
                return user
