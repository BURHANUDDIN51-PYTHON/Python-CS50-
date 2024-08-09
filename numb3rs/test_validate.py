from numb3rs import validate
def test_validate():
    assert validate('1.25.9.0') == True
    
if __name__ == "__main__":
    main()