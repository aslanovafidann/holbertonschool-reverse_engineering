:\autounattend.xml",
        r"C:\Windows\Panther\Unattend.xml"
    ]


    print("Searching for administrative password in unattended files...")
    password = check_multiple_paths_for_password(possible_paths)


    if password:
        print(f"Final decoded password: {password}")
    else:
        print("No password found in any of the paths.")


if __name__ == "__main__":
    main()
