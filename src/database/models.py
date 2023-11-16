from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Bill(Base):
    __tablename__ = 'bills'

    id = Column(Integer, primary_key=True)
    bill_number = Column(String(50), unique=True, nullable=False, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    introduced_date = Column(DateTime, default=datetime.utcnow)
    last_action_date = Column(DateTime, default=datetime.utcnow)
    last_action = Column(String(255), nullable=True)
    status = Column(String(100), nullable=False)
    sponsor_id = Column(Integer, ForeignKey('sponsors.id'), nullable=True)
    sponsor = relationship("Sponsor", back_populates="bills")
    votes = relationship("Vote", back_populates="bill")

    def __repr__(self):
        return f"<Bill(bill_number='{self.bill_number}', title='{self.title}', status='{self.status}')>"

class Sponsor(Base):
    __tablename__ = 'sponsors'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    district = Column(String(100), nullable=True)
    party = Column(String(50), nullable=True)
    bills = relationship("Bill", order_by=Bill.id, back_populates="sponsor")

    def __repr__(self):
        return f"<Sponsor(name='{self.name}', district='{self.district}', party='{self.party}')>"

class Vote(Base):
    __tablename__ = 'votes'

    id = Column(Integer, primary_key=True)
    bill_id = Column(Integer, ForeignKey('bills.id'), nullable=False)
    bill = relationship("Bill", back_populates="votes")
    voter_name = Column(String(255), nullable=False)
    vote = Column(String(10), nullable=False)  # For example, 'Yea', 'Nay', 'Abstain'
    date = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Vote(bill_id={self.bill_id}, voter_name='{self.voter_name}', vote='{self.vote}')>"

# Additional classes like Committee, Amendment, etc. can be added here as needed.
