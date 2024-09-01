export interface Book {
  id: number;
  title: string;
  author: string;
  short_description: string;
  genre: string;
  cover_photo_url: string;
  publication_year: number;
  likes: number;
  liked_by_user: boolean
}
