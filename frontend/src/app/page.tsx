import CreateNote from "@/components/Note/Add";
import RecentlyViewed from "@/components/RecentlyViewed";

const Home = () => {
  return (
    <main className="flex flex-col w-full text-white overflow-hidden">
      <CreateNote />
      <RecentlyViewed />
    </main>
  );
};

export default Home;
