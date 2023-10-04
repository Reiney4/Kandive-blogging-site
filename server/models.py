# Imported the necessary files
from sqlalchemy.orm import validates
from sqlalchemy import MetaData, ForeignKey
from flask_sqlalchemy import SQLAlchemy

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Define a one-to-many relationship with Hero_powers
    blogposts = db.relationship('User_blogposts', back_populates='user')

    def __repr__(self):
        return f'(id={self.id}, name={self.name} email={self.email})'


class Blogpost(db.Model):
    __tablename__ = 'blogposts '

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    description = db.Column(db.String(100))
    strength = db.Column(db.String())
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Define a one-to-many relationship with Hero_powers
    users = db.relationship('User_blogposts', back_populates='blogpost')

    def __repr__(self):
        return f'(id={self.id}, name={self.name} description={self.description})'

    @validates('description')
    def checks_description(self, key, description):
        if len(description) < 20:
            raise ValueError("Description must be longer than 20 chars")
        else:
            return description
        

class User_blogposts(db.Model):
    __tablename__ = 'user_blogposts'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(120))
    user_id = db.Column(db.Integer, ForeignKey('users.id'))
    blogpost_id = db.Column(db.Integer, ForeignKey('blogposts.id'))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # Define many-to-one relationships with Hero and Power
    user = db.relationship('User', back_populates='blogposts')
    blogpost = db.relationship('Blogpost', back_populates='users')

def __repr__(self):
        return f'(id={self.id}, userID={self.user_id} strength={self.strength}) blogpostID={self.blogpost_id}'

@validates('strength')
def checks_strength(self, key, strength):
        if strength not in ['Strong', 'Weak', 'Average']:
            raise ValueError("Strength must be a value either 'Strong', 'Weak' or 'Average'")
        else:
            return strength