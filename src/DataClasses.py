from dataclasses import dataclass, field
from typing import List
import datetime


@dataclass
class Movie:
    id: int
    collection_id: int
    budget: int
    homepage: str
    imdb_id: str
    original_language_id: int
    original_title: str
    overview: str
    popularity: float
    poster_path: str
    release_date: datetime.date
    runtime: int
    status: str
    tagline: str
    title: str
    revenue: int
    production_company_ids: List[int] = field(default_factory=list)
    production_country_ids: List[int] = field(default_factory=list)
    keyword_ids: List[int] = field(default_factory=list)
    cast_ids: List[int] = field(default_factory=list)
    crew_ids: List[int] = field(default_factory=list)
    spoken_language_ids: List[int] = field(default_factory=list)
    genre_ids: List[int] = field(default_factory=list)
    table_name: str = 'tmdb_movies'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"{self.collection_id}, "
                f"{self.budget}, "
                f"{self.genre_ids}, "
                f"$${self.homepage}$$, "
                f"{self.imdb_id}, "
                f"{self.original_language_id}, "
                f"$${self.original_title}$$, "
                f"$${self.overview}$$, "
                f"{self.popularity}, "
                f"$${self.poster_path}$$, "
                f"{self.production_company_ids}, "
                f"{self.production_country_ids}, "
                f"{self.release_date}, "
                f"{self.runtime}, "
                f"{self.spoken_language_ids}, "
                f"$${self.status}$$, "
                f"$${self.tagline}$$, "
                f"$${self.title}$$, "
                f"{self.keyword_ids}, "
                f"{self.cast_ids}, "
                f"{self.crew_ids}, "
                f"{self.revenue}) ON CONFLICT (id) DO NOTHING")


@dataclass
class Collection:
    id: int
    name: str
    poster_path: str
    backdrop_path: str
    table_name: str = 'tmdb_collection'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"$${self.name}$$, "
                f"$${self.poster_path}$$, "
                f"$${self.backdrop_path}$$) ON CONFLICT (id) DO NOTHING")


@dataclass
class Genre:
    id: int
    name: str
    table_name: str = 'tmdb_genres'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")


@dataclass
class ProductionCompany:
    id: int
    name: str
    table_name: str = 'tmdb_production_companies'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")


@dataclass
class Country:
    iso_3166_1: str
    name: str
    table_name: str = 'tmdb_countries'
    id: int = None

    def get_insert_statement(self) -> str:
        if self.id is None:
            return (f"INSERT INTO {self.table_name}(iso_3166_1, name) VALUES($${self.iso_3166_1}$$, "
                    f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")
        else:
            return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"$${self.iso_3166_1}$$, "
                f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")


@dataclass
class Language:
    iso_639_1: str
    name: str
    table_name: str = 'tmdb_languages'
    id: int = None

    def get_insert_statement(self) -> str:
        if self.id is None:
            return (f"INSERT INTO {self.table_name}(iso_639_1, name) VALUES($${self.iso_639_1}$$, "
                    f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")
        else:
            return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"$${self.iso_639_1}$$, "
                f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")


@dataclass
class Keyword:
    id: int
    name: str
    table_name: str = 'tmdb_keywords'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"$${self.name}$$) ON CONFLICT (id) DO NOTHING")


@dataclass
class Cast:
    id: int
    movie_id: int
    cast_id: int
    credit_id: str
    character: str
    gender: int
    name: str
    order: int
    profile_path: str
    table_name: str = 'tmdb_cast'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"{self.movie_id}, "
                f"{self.cast_id}, "
                f"$${self.credit_id}$$, "
                f"ARRAY[$${'$$, '.join(self.character.split('/'))}$$], "
                f"$${self.gender}$$, "
                f"$${self.name}$$, "
                f"{self.order}, "
                f"$${self.profile_path}$$) ON CONFLICT (id, movie_id) DO NOTHING")


@dataclass
class Crew:
    id: int
    movie_id: int
    credit_id: str
    department: str
    gender: int
    job: str
    name: str
    profile_path: str
    table_name: str = 'tmdb_crew'

    def get_insert_statement(self) -> str:
        return (f"INSERT INTO {self.table_name} VALUES({self.id}, "
                f"{self.movie_id}, "
                f"$${self.credit_id}$$, "
                f"$${self.department}$$, "
                f"$${self.gender}$$, "
                f"$${self.job}$$, "
                f"$${self.name}$$, "
                f"$${self.profile_path}$$) ON CONFLICT (id, movie_id) DO NOTHING")
