"use client";

import { useEffect, useState } from "react";

import { faNoteSticky } from "@fortawesome/free-regular-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import Note from "../Notes/Cards";

const RecentlyViewed = () => {
  const [notes, setNotes] = useState<NoteProps[]>([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/notes/")
      .then((res) => res.json())
      .then((data) => setNotes(data));
  }, []);

  return (
    <aside className="mt-8 flex flex-col justify-center">
      <section className="flex text-2xl">
        <FontAwesomeIcon icon={faNoteSticky} width={25} height={25} />
        <span className="ml-2">My Notes</span>
      </section>
      <p className="opacity-60"> Recently Viewed </p>
      <section className="flex mt-4 gap-6">
        {notes.map((note) => (
          <Note
            body={note.body}
            title={note.title}
            createdAt={note.createdAt}
            id={note.id}
            updatedAt={note.updatedAt}
            key={note.id}
          />
        ))}
      </section>
    </aside>
  );
};

export default RecentlyViewed;
