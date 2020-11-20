from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
    builder = ConanMultiPackager(pure_c=False)
    builder.add_common_builds()
    builder.run()
