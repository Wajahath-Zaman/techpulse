from src.scrapers.techcrunch.integrator import TechCrunchIntegrator


def main():
    integrator = TechCrunchIntegrator()

    integrator.run()


if __name__ == "__main__":
    main()