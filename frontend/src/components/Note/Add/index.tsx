const CreateNote = () => {
  return (
    <section className="h-[350px] w-full shadow-sm shadow-black p-10 flex flex-col gap-4">
      <h1 className="text-4xl">Add a Note</h1>
      <input className="bg-transparent outline-none" placeholder="Title" />
      <input
        className="bg-transparent outline-none"
        placeholder="Take a note..."
      />
    </section>
  );
};

export default CreateNote;
