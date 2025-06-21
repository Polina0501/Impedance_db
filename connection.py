from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Date, DateTime, Time
from sqlalchemy.orm import sessionmaker, DeclarativeBase, relationship

engine = create_engine(f'postgresql+psycopg2://postgres:1234@localhost:5432/Impedance_db', echo=True)
Session = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass


class Experiment(Base):
    __tablename__ = 'experiment'

    id = Column(Integer, primary_key=True)
    material_id = Column(Integer, ForeignKey('material.id'), nullable=False)
    experiment_num = Column(Integer, nullable=False)
    experiment_time = Column(Time, nullable=False)

    material = relationship('Material', back_populates='experiments')
    measures = relationship('Measure', back_populates='experiment', cascade='all, delete-orphan')


class Material(Base):
    __tablename__ = 'material'

    id = Column(Integer, primary_key=True)
    date_exp = Column(Date, nullable=False)
    electrolyte_percentage_1 = Column(Float, nullable=False)
    electrolyte_material_1 = Column(String, nullable=False)
    electrolyte_percentage_2 = Column(Float, nullable=False)
    electrolyte_material_2 = Column(String, nullable=False)
    electrolyte_thickness = Column(Float, nullable=False)
    electrode_percentage_1 = Column(Float, nullable=False)
    electrode_material_1 = Column(String, nullable=False)
    electrode_percentage_2 = Column(Float, nullable=False)
    electrode_material_2 = Column(String, nullable=False)
    electrode_starch_percentage = Column(Float, nullable=False)
    electrode_thickness = Column(Float, nullable=False)

    experiments = relationship('Experiment', back_populates='material', cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.electrolyte_material_1} - {self.electrolyte_percentage_1} ; {self.electrolyte_material_2} - {self.electrolyte_percentage_2}'


class Measure(Base):
    __tablename__ = 'measure'

    id = Column(Integer, primary_key=True)
    experiment_id = Column(Integer, ForeignKey('experiment.id'), nullable=False)
    re = Column(Float, nullable=False)
    im = Column(Float, nullable=False)
    f = Column(Float, nullable=False)
    point_num = Column(Integer, nullable=False)

    experiment = relationship('Experiment', back_populates='measures')


if __name__ == '__main__':
    # Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

# Полиночка самая лучшая, она молодецмау!
